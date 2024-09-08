def on_forever():
    global light_level
    light_level = Kitronik_LAMPbit.light_level()
    if light_level < 50:
        Kitronik_LAMPbit.lamp_light_led(Kitronik_LAMPbit.DisplayLamp.ON)
    elif light_level > 50:
        Kitronik_LAMPbit.lamp_light_led(Kitronik_LAMPbit.DisplayLamp.OFF)
    basic.show_number(light_level)
light_level = 0
Kitronik_LAMPbit.deadband_input(25)
# basic.forever(on_forever)

def on_forever2():
    Kitronik_STOPbit.traffic_light_state(Kitronik_STOPbit.LightStates.STOP)
    basic.show_number(5)
basic.forever(on_forever2)
