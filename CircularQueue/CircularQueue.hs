import qualified Data.Vector                   as V
import           Data.Vector.Mutable            ( write )
data CircularQueue a = CircularQueue
  { queueValues :: V.Vector (Maybe a)
  , queueFront  :: Int
  , queueRear   :: Int
  }
  deriving (Show, Eq)

modifyVec :: Int -> a -> V.Vector a -> V.Vector a
modifyVec i e v = V.modify (\mv -> write mv i e) v

qLength = length . queueValues

queueFromList :: [a] -> CircularQueue a
queueFromList list = CircularQueue (Just <$> V.fromList list) 0 0


createQueue :: Int -> CircularQueue a
createQueue size = CircularQueue (V.replicate size Nothing) 0 0

append :: CircularQueue a -> a -> Maybe (CircularQueue a)
append q elem
  | queueRear q == qLength q = Nothing
  | otherwise = Just $ CircularQueue
    { queueValues = modifyVec (queueRear q) (Just elem) (queueValues q)
    , queueFront  = queueFront q
    , queueRear   = (1 + queueRear q) `mod` qLength q
    }

pop :: CircularQueue a -> (Maybe a, CircularQueue a)
pop q
  | queueFront q == qLength q
  = (Nothing, q)
  | otherwise
  = ( queueValues q V.! queueFront q
    , CircularQueue
      { queueValues = modifyVec (queueFront q) (Nothing) (queueValues q)
      , queueFront  = (1 + queueFront q) `mod` qLength q
      , queueRear   = queueRear q
      }
    )

main :: IO ()
main = do
  let popped = pop $ queueFromList ["a", "b", "c", "d"]

  print popped
