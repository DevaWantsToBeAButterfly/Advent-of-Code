puzzleInput = [2, 1, 1, 4, 4, 1, 3, 4, 2, 4, 2, 1, 1, 4, 3, 5, 1, 1, 5, 1, 1, 5, 4, 5, 4, 1, 5, 1, 3, 1, 4, 2, 3, 2, 1, 2, 5, 5, 2, 3, 1, 2, 3, 3, 1, 4, 3, 1, 1, 1, 1, 5, 2, 1, 1, 1, 5, 3, 3, 2, 1, 4, 1, 1, 1, 3, 1, 1, 5, 5, 1, 4, 4, 4, 4, 5, 1, 5, 1, 1, 5, 5, 2, 2, 5, 4, 1, 5, 4, 1, 4, 1, 1, 1, 1, 5, 3, 2, 4, 1, 1, 1, 4, 4, 1, 2, 1, 1, 5, 2, 1, 1, 1, 4, 4, 4, 4, 3, 3, 1, 1, 5, 1, 5, 2, 1, 4, 1, 2, 4, 4, 4, 4, 2, 2, 2, 4, 4, 4, 2, 1, 5, 5, 2, 1, 1, 1, 4, 4, 1, 4, 2, 3, 3, 3, 3, 3, 5, 4, 1, 5, 1, 4, 5, 5, 1, 1, 1, 4, 1, 2, 4, 4, 1, 2, 3, 3, 3, 3, 5, 1, 4, 2, 5, 5, 2, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 2, 5, 4, 2, 1, 1, 2, 2, 2, 1, 3, 1, 5, 4, 1, 1, 5, 3, 3, 2, 2, 3, 1, 1, 1, 1, 2, 4, 2, 2, 5, 1, 2, 4, 2, 1, 1, 3, 2, 5, 5, 3, 1, 3, 3, 1, 4, 1, 1, 5, 5, 1, 5, 4, 1, 1, 1, 1, 2, 3, 3, 1, 2, 3, 1, 5, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 5, 1, 1, 5, 5, 2, 1, 1, 5, 2, 4, 5, 5, 1, 1, 5, 1, 5, 5, 1, 1, 3, 3, 1, 1, 3, 1]

testInput = [3, 4, 3, 1, 2]
newborns = 0

function simulateDay(inputArray) {
	for (let i = 0; i < inputArray.length; i++) {
		if (inputArray[i] === 0) {
			inputArray[i] = 6
			newborns++
		} else {
			inputArray[i]--
		}
	}

	while (newborns) {
		inputArray.push(8)
		newborns--
	}
}

function runSimulation(inputArray, days) {
	for (let day = 1; day <= days; day++) {
		console.log('Running simulation for day ' + day)
		simulateDay(inputArray)
	}

	console.log(inputArray.length)

}


runSimulation(testInput, 80)
