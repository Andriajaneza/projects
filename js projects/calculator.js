var num1 = (
                '2'   //<-- enter first number here
)
var opperator = (
                '+'   //<-- enter opperator here
)

var num2 = (
                '2'   //<-- enter second number here
)

var A = (parseFloat(num1))
var B = (parseFloat(num2))

if (opperator === '+') {
    console.log(A + B)
}
else if (opperator === '-') {
    console.log(A - B)
}
else if (opperator === '/') {
    console.log(A / B)
}
else if (opperator === '*') {
    console.log(A * B)
}
else {
    console.log("Invalid operation");
}