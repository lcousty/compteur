input.onButtonPressed(Button.A, function () {
    if (Cpt <= MAX) {
        // 10 est une constante est un magic number
        Cpt += 1
    }
})
input.onButtonPressed(Button.B, function () {
    if (Cpt > 0) {
        Cpt += -1
    }
})
let MAX = 0
let Cpt = 0
// déclaration de la variable et initialisation
Cpt = 0
MAX = 10
// valeur maximale dans le bus
basic.forever(function () {
    basic.showNumber(Cpt)
})
