import java.util.*
import kotlin.system.measureTimeMillis

fun main()
{
	val seqTime = measureTimeMillis {
		val randoms = getRandomNumbers(100_000_000)
	}
	println("Sequential Took $seqTime ms")

	val parallelTime = measureTimeMillis {
		val randoms = getRandomNumbersAsync(100_000_000)
	}
	println("Parallel Took $parallelTime ms")
}


fun getRandomNumbers(count: Int, min: Int = 1, max: Int = 6): IntArray
{
	val random = SplittableRandom()
	val numbers = IntArray(6)
	for (i in 0..count)
	{
		val rand = random.nextInt(min, max + 1)
		numbers[rand - 1] += 1
	}
	return numbers
}

fun getRandomNumbersAsync(count: Int, min: Int = 1, max: Int = 6): IntArray
{
	val random = SplittableRandom()
	val numbers = IntArray(6)
	for (i in random.ints(count.toLong(), min, max + 1))
	{
		numbers[i - 1] += 1
	}
	return numbers
}
