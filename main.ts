function on_forever () {
    light_level = Kitronik_LAMPbit.lightLevel()
    if (light_level < 50) {
        Kitronik_LAMPbit.lampLightLED(Kitronik_LAMPbit.DisplayLamp.On)
    } else if (light_level > 50) {
        Kitronik_LAMPbit.lampLightLED(Kitronik_LAMPbit.DisplayLamp.Off)
    }
    basic.showNumber(light_level)
}
let light_level = 0
Kitronik_LAMPbit.deadbandInput(25)
// basic.forever(on_forever)
basic.forever(function () {
    Kitronik_STOPbit.trafficLightState(Kitronik_STOPbit.LightStates.Stop)
    basic.showNumber(5)
})
