input.onGesture(Gesture.LogoDown, function () {
    basic.showNumber(ahmed1 - ahmed2)
})
input.onButtonPressed(Button.A, function () {
    ahmed1 = 1
    basic.showNumber(ahmed1)
})
input.onButtonPressed(Button.AB, function () {
    ahmed1 = 0
    ahmed2 = 0
    basic.clearScreen()
})
input.onGesture(Gesture.LogoUp, function () {
    basic.showNumber(ahmed1 + ahmed2)
})
input.onButtonPressed(Button.B, function () {
    ahmed2 = 1
    basic.showNumber(ahmed2)
})
let ahmed2 = 0
let ahmed1 = 0
ahmed1 = 0
ahmed2 = 0
