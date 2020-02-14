#!/usr/bin/python3
start_program = input("Would you like to perform diagnostics on your car? y/n\n")
if start_program == ("y"):
   yesno = input("Test number 1: Starter cranks?\n")
   if yesno == "n":
        starter_spins = input("Test number 2: Starter spins?\n")
        if starter_spins == "y":
            print("Diagnosis is:  Solenoid stuck, not powered. Missing teeth on flywheel.")
        elif starter_spins == "n":
            battery_read = input("Test number 3: Battery read over 12V?\n")
            if battery_read == "n":
                print("Diagnosis is:  Jumpstart or pop start car and check if battery is charging.")
            elif battery_read == "y":
                clean_terminals = input("Test number 4: Cleaned terminals?\n")
                if clean_terminals == "y":
                    print("Diagnosis is:  With car in park or neutral, use heavy jumper or screwdriver to bypass starter relay solenoid. Test starter.")
                elif clean_terminals == "n":
                    print("Diagnosis is:  Clean battery terminals and connectors, engine ground.")
   if yesno == "y":
        engine_fires = input("Test number 2: Engine fires?\n")
        if engine_fires == "y":
            starts_stalls = input("Test number 3: Starts and stalls?\n")
            if starts_stalls == "n":
                print("Diagnosis is:  Ignition timing, fuel problem, cranking too slow - battery, starter.")
            elif starts_stalls == "y":
                OBD_blink = input("Test number 4: Check OBD, blink code?\n")
                if OBD_blink == "n":
                    print("Diagnosis is:  Read OBD or OBD II or check for blink code access.")
                elif OBD_blink == "y":
                    stall_release = input("Test number 5: Stalls on key release to run?\n")
                    if stall_release == "y":
                        print('Diagnosis is:  Ignition "run" circuit or column key switch failure. Ring out with meter.')
                    elif stall_release == "n":
                        stall_rain = input("Test number 6: Stalls in rain?\n")
                        if stall_rain == "y":
                            print("Diagnosis is:  Check for cracked coil, distributor. Check visible electrical arcing running in dark.")
                        elif stall_rain == "n":
                            stall_warm = input("Test number 7: Stalls warm?\n")
                            if stall_warm == "n":
                                print("Diagnosis is:  On cold stalling, check for stuck choke, EGR. Check for vacuum leak.")
                            elif stall_warm == "y":
                                print("Diagnosis is:  Adjust idle, blow out fuel filter, check fuel pump output. Check vacuum leak or sensor failure.")
        elif engine_fires == "n":
            spark_plug = input("Test number 3: Spark to plugs?\n")
            if spark_plug == "y":
                fuel_filter = input("Test number 4: Fuel to filter?\n")
                if fuel_filter == "n":
                    print("Diagnosis is:  Vapor lock, fuel pump, blockage.")
                elif fuel_filter == "y":
                    fuel_inject = input("Test number 5: Fuel injected?\n")
                    if fuel_inject == "y":
                        print("Diagnosis is:  Single point, check throttle body. Electronic multipoint, separate diagonstic.")
                    elif fuel_inject == "n":
                        print("Diagnosis is:  Try starter spray in carb, throttle open.")
            elif spark_plug == "n":
                spark_coil = input("Test number 4: Spark from coil?\n")
                if spark_coil == "n":
                    volt_primary = input("Test number 5: 12V+ at coil primary?\n")
                    if volt_primary == "y":
                        print("Diagnosis is:  Test coil for internal short. Check secondary output wire resistance.")
                    elif volt_primary == "n":
                        print("Diagnosis is:  Ignition system wiring, voltage regulator.")
                if spark_coil == "y":
                    mech_dist = input("Test number 5: Mechanical distributor?\n")
                    if mech_dist == "y":
                        print("Diagnosis is:  Check condenser, points or magnetic pick-up, rotor, or cap damage.")
                    elif mech_dist == "n":
                        print("Diagnosis is:  For electronic distribution, see model manual for diagnostic checks.")
else:
    quit()


