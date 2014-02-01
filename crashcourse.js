// add your javascript code here

console.log('Hello, console!');

// Exercises (part 1)
function max(a, b) {
    return a>b ? a: b;

    if (a>b) {
    	return a;
    }else {
    	return b;
    }
}

function fibonacci(n) {
	function fibhelper(n, a, b) {
		if (n ==0) return 0;
		else if (n==1) return 1;
		else return fibonacci(n-1)+fibonacci(n-2)
	}
	return fibhelper(n, a, b)
	
}

//recursive function which returns the nth fibonacci number

function charFreq(str) {
	var charFreq={}:
	for (var i =0); i<str.length; i++) {
		if (!charMap[str[i]]) {
			charMap[str[i]] = 0;
		}

		charMap[stri[i]]++;
	}
	return CharMap;

}

//returns an object containing the frequency of character in the string
//Example: charFreq("bob") returns ["b": 2, "o": 1]


// Exercises (part 2)
function memoize(f) {
	var vals = {};
	return function(x) {
		if (vals[x] !== undefined) {
			return vals[x];
		} else {
			var 
		}
	}

}

//takes a function f and returns a function g such that the input/output of every call to g is saved in a dictionary and used if possible

function map(obj, f) {
    
}

//takes an object obj and a function f and applies f to every value in obj
