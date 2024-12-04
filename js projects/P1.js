// project #1 calculator

var num1 = (
                '1'   //<-- enter first number here
)
var opperator = (
                '+'   //<-- enter opperator here
)

var num2 = (
                '1'   //<-- enter second number here
)

var A = (parseFloat(num1))
var B = (parseFloat(num2))

if (opperator == '+') {
    console.log(A + B)
}
else if (opperator == '-') {
    console.log(A - B)
}
else if (opperator == '/') {
    console.log(A / B)
}
else if (opperator == '*') {
    console.log(A * B)
}
else {
    console.log("Invalid operation");
}