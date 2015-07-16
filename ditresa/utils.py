
#----------------------------------------------------------------------
def user_session(request):
    ''' Request username from session '''
    if request.session.get('username'):
        username = request.session.get('username')
    else:
        username = None
    return username 


#----------------------------------------------------------------------
def edit_permision(request, video):
    """Check if author and editor is the same person."""
    # video = get_object_or_404(Video, pk=video_id)
    logged_user = request.session["username"]
    author_user = video.user.username
    print(logged_user + ' == ' + author_user)
    if logged_user == author_user:
        return ("")
    else:
        return ("readonly")


#----------------------------------------------------------------------
def level_calc_manager(natal_tab, control_tab, esolevel, planets12):
    """ Manage calculation of planet levels and planet control combinations.
        'planets' is a list of used planets in the right order.
    """
    planet_control = { k: control_tab[natal_tab[k]][esolevel] 
                       for k in natal_tab }    
    planet_level, used_planets = calc_level(planet_control)
    planets = [item for item in planets12 if item in used_planets]
    return (planets, planet_control, planet_level)


#----------------------------------------------------------------------
def calc_level(planet_control):
    """Calculation of the planet levels"""
    planet_control_keys = (planet_control.keys())
    planet_control_values = (planet_control.values())
    used_planets = []
    planet_levels = [[]]
    planet_level_dict = {}
    left_control_keys = list(planet_control_keys)

    # 0-level planets extracting (0-level without cycle)
    level = 0
    for planet in planet_control_keys:
        planet_value = planet_control[planet]
        if (planet_value == 'Vul') or (planet_value == 'Ear') or (planet 
                        == planet_value):
            level_fix(planet, used_planets, planet_levels, left_control_keys, 
                    planet_control, level, planet_level_dict)
    
    # 0-level planets extracting (0-level with cycle)
    for planet in left_control_keys:
        planet_cycle = []
        finish = False
        index = 0
        while (finish == False) and (index < 10):
            if not planet_cycle:
                base_cycle_planet = planet
                planet_cycle.append(planet)
 
            next_cycle_planet = planet_control[planet_cycle[index]]
            if next_cycle_planet not in planet_levels[0]:
                if next_cycle_planet in planet_cycle:
                    index_begin = planet_cycle.index(next_cycle_planet)
                    planet_cycle = planet_cycle[index_begin:]

                    # Function for cycle
                    level_fix_cycle (planet, used_planets, planet_levels, 
                                    left_control_keys, planet_control, 
                                    planet_cycle, level, planet_level_dict)
                    

                    break            
                else:                        # cycle is closed
                    planet_cycle.append(next_cycle_planet)
            else:                            # found second level from cycle
                break

            index += 1
            

    # 1- and more-level planets extracting
    finish = False
    level = 1
    fuse = 0
    while (finish == False) and (fuse < 12):
        try:
            for planet in planet_control_keys:
                if left_control_keys == []:
                    finish = True
                    break
                elif planet in left_control_keys:
                    if planet_control[planet] in planet_levels[level-1]:
                        level_fix(planet, used_planets, planet_levels, 
                                  left_control_keys, planet_control, level, 
                                  planet_level_dict)
        except IndexError:
            print ('Error - there is no planets in previous level')
            break  
                      
        level += 1
        fuse += 1                 # Defender against infinite cycle

    # print(' =============== Data output from function ================ ')
    # print ('left_control_keys = ', left_control_keys)
    # print ('used_planets = ', used_planets)
    # print ('planet_levels = ', planet_levels)
    # print ('planet_level_dict = ', planet_level_dict)
    
    return (planet_level_dict, used_planets)

#----------------------------------------------------------------------
def level_fix_cycle(planet, used_planets, planet_levels, left_control_keys, 
                    planet_control, planet_cycle, level, planet_level_dict):
    """Calculation of the planet levels - 0-level for cycle"""
    for planet in planet_cycle:
        used_planets.append(planet)       # Add planet to the used planet list  
        planet_levels[level].append(planet)
        planet_level_dict[planet] = level
        if planet in left_control_keys:
            left_control_keys.remove(planet)  # Delete from left planet list


#----------------------------------------------------------------------
def level_fix(planet, used_planets, planet_levels, left_control_keys, 
              planet_control, level, planet_level_dict):
    """Calculation of the planet levels"""
    planet_value = planet_control[planet]
    if len(planet_levels) < (level+1):
        planet_levels.append([])
    if (planet_value == 'Vul') or (planet_value == 'Ear'):
        if level == 0:
            used_planets.append(planet_value) # Add to used planet list
            planet_levels[level].append(planet_value) #Add planet to the level 
            planet_level_dict[planet_value] = level       
        else:
            used_planets.append(planet)   # Add planet to the used planet list
            planet_levels[level].append(planet)   # Add planet to the level
            planet_level_dict[planet] = level        
            if planet in left_control_keys:
                left_control_keys.remove(planet) #Delete from left planet list
    else:
        used_planets.append(planet)
        planet_levels[level].append(planet)   # Add planet to the level
        planet_level_dict[planet] = level
        if planet in left_control_keys:
            left_control_keys.remove(planet)  # Delete from left planet list

