package randomdice

import java.util.*
import java.util.stream.Collectors
import kotlin.system.measureTimeMillis

const val times = 100
inline fun measureAverageTime(task: () -> Unit): Long
{
	var total = 0L
	repeat(times) {
		val taskTime = measureTimeMillis(task)
		total += taskTime
	}
	return total / times
}

fun main()
{
	val seqTime = measureAverageTime {
		val randoms = getRandomNumbers(100_000_000)
		randoms.first() //prevent potential compiler optimizations
	}
	println("Sequential Took an average of $seqTime ms")

	val parallelTime = measureAverageTime {
		val randoms = getRandomNumbersParallel(100_000_000)
		randoms.first() //prevent potential compiler optimizations
	}
	println("Parallel Streams took an average of $parallelTime ms")
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

fun getRandomNumbersParallel(count: Int, min: Int = 1, max: Int = 6): LongArray
{
	val random = SplittableRandom()
	val numbers = LongArray(6)
	val counts = random.ints(count.toLong(), min, max + 1)
			.parallel()
			.boxed()
			.collect(Collectors.groupingBy({ it }, Collectors.counting()))

	counts.forEach {
		numbers[it.key - 1] = it.value
	}
	return numbers
}
