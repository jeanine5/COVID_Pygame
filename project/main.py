"""CSC110 Fall 2021 Final Assignment: Stress and Spending Interactive Game

===============================
Project program due Dec 14 2021. This file contains all the code to run the game. It imports
the function all_graphs from game_data_graphs to display in the browser and
change_in_essentials_monthly and change_in_nonessentials_monthly from change_computations.py
These functions are used for analysis as mentioned in the Computational Plan section of the Project
overview.

Copyright and Usage Information
===============================

This file is Copyright (c) 2021 Jeanine Colleen Ohene-Agyei, Luke Ham, Chelsea Wang, and Bolin Shen.
"""

# Import the pygame module
import pygame
from sys import exit
from game_data_graphs import all_graphs
from change_computations import change_in_essentials_monthly, change_in_nonessentials_monthly

# Initialize pygame and font for all text
pygame.init()
screen = pygame.display.set_mode((1450, 900))
pygame.display.set_caption('Stress and Spending')
test_font = pygame.font.Font(None, 30)

# intial coords for some surfaces so they can be altered during the main while loop.
graph_coords = (2000, 2000)
stress_coords = (2000, 2000)
house_coords = (-15, -35)
parent_coords = (2000, 2000)
text_coords = (420, 100)
text2_coords = (50, 100)

# the background and pixel parent for the game. Parent surface not set bc it depends on user.
background_surface = pygame.image.load("background.png")
house_surface = pygame.image.load("House.png")
parent_surface = pygame.image.load('background.png')

# creating size for the datasets displayed.
graph = pygame.transform.scale(pygame.image.load('Graph_display.png'), (620, 340))
stress = pygame.transform.scale(pygame.image.load('stress_display.png'), (400, 300))

# list intended for collecting user data
stress_percentage = []
amount = []
essentials = []
non_essentials = []

# scenarios for the game
scenarios = ['MARCH 2020: Use $ 200 on kids games and entertainment or $ 150 on COVID safety '
             'supplies',
             'APRIL 2020: Use $ 100 on new kids TV subscription or $ 300 on WIFI for kids online '
             'learning',
             'MAY 2020: Use $ 1200 on tire and oil changes or $ 2500 on new laptops for kids online '
             'learning',
             'JUNE 2020: Use $ 60 for family trip to lake or $ 200 on N-95 masks and face shields',
             'JULY 2020: Use $ 250 for nice family outdoor restaurant or $ 100 on groceries',
             'AUGUST 2020: Use $ 530 on fun overseas family trip or $ 40 on COVID test for optional '
             'work opportunity',
             'SEPTEMBER 2020: Use $ 120 for night at movie theater or $ 200 on more COVID supplies',
             '[LEFT/RIGHT KEY TO SEE THE GRAPHS]']

# fluctuating rates for covid
covid_rates = ['COVID RATES HIGH, MASKS REQUIRED', 'COVID RATES HIGH, MASKS REQUIRED',
               'COVID RATES HIGH, MASKS REQUIRED', 'COVID RATES PEAK, MASKS REQUIRED',
               'COVID RATES LOWER, MASKS REQUIRED', 'COVID RATES LOWER, SOME MASKS REQUIREMENTS '
                                                    'LIFTED',
               'COVID RATES SIGNIFICANTLY LOWER, SOME MASKS REQUIREMENTS LIFTED', '']

# the timeline for the game. This will be the x-axis for the graphs
time = ['MARCH 2020', 'APRIL 2020', 'MAY 2020', 'JUNE 2020', 'JULY 2020', 'AUGUST 2020',
        'SEPTEMBER 2020']

# the headings for the last screen before the graphs
april = test_font.render('  ', False, (0, 0, 0))
may = test_font.render('  ', False, (0, 0, 0))
june = test_font.render('  ', False, (0, 0, 0))
july = test_font.render('  ', False, (0, 0, 0))
august = test_font.render('  ', False, (0, 0, 0))
september = test_font.render('  ', False, (0, 0, 0))

# essential headings for each month on last screen before the graphs
ap_essentials = test_font.render('  ', False, (0, 0, 0))
may_essentials = test_font.render('  ', False, (0, 0, 0))
july_essentials = test_font.render('  ', False, (0, 0, 0))
june_essentials = test_font.render('  ', False, (0, 0, 0))
aug_essentials = test_font.render('  ', False, (0, 0, 0))
sept_essentials = test_font.render('  ', False, (0, 0, 0))

# non-essential headings for each month on last screen before the graphs
ap_nonessentials = test_font.render('  ', False, (0, 0, 0))
may_nonessentials = test_font.render('  ', False, (0, 0, 0))
june_nonessentials = test_font.render('  ', False, (0, 0, 0))
july_nonessentials = test_font.render('  ', False, (0, 0, 0))
aug_nonessentials = test_font.render('  ', False, (0, 0, 0))
sept_nonessentials = test_font.render('  ', False, (0, 0, 0))

# the values that will be place next to the essent./non-essent. headings for each month
ap_e1 = test_font.render('  ', False, (0, 0, 0))
ap_none1 = test_font.render('  ', False, (0, 0, 0))
may_e1 = test_font.render('  ', False, (0, 0, 0))
may_none1 = test_font.render('  ', False, (0, 0, 0))
june_e1 = test_font.render('  ', False, (0, 0, 0))
june_none1 = test_font.render('  ', False, (0, 0, 0))
july_e1 = test_font.render('  ', False, (0, 0, 0))
july_none1 = test_font.render('  ', False, (0, 0, 0))
aug_e1 = test_font.render('  ', False, (0, 0, 0))
aug_none1 = test_font.render('  ', False, (0, 0, 0))
sept_e1 = test_font.render('  ', False, (0, 0, 0))
sept_none1 = test_font.render('  ', False, (0, 0, 0))

# text variables created so they can be used inside and outside for loop
text_surface = test_font.render('Up Key for lone parent, Down Key for coupled parent',
                                False, (0, 0, 0))
text_surface2 = test_font.render(' ', False, (0, 0, 0))
rates = test_font.render('  ', False, (0, 0, 0))
amount_left = test_font.render('  ', False, (0, 0, 0))
stress_levels = test_font.render('  ', False, (0, 0, 0))
avg_spending_essential = test_font.render('  ', False, (0, 0, 0))
avg_spending_nonessential = test_font.render('  ', False, (0, 0, 0))

# couldn't use index-based loop so created a count variable that will increase 1 per loop
scenario_count = 0

# Main loop - all code for game must go in this loop
while True:
    # what action must come next if user hits a key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if player hits any defined key down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                test_font = pygame.font.Font(None, 27)
                text_surface = test_font.render(' ', False, (0, 0, 0))
                text_surface2 = test_font.render('You are a lone parent. For each scenario, '
                                                 'use LEFT KEY to select FIRST OPTION and use RIGHT'
                                                 ' KEY to select SECOND OPTION [SPACE TO CONTINUE]',
                                                 False, (0, 0, 0))
                parent_coords = (650, 250)
                parent_surface = pygame.transform.scale(pygame.image.load("single_parent.jpg"),
                                                        (170, 130))
                test_font = pygame.font.Font(None, 30)
                # collects the initial user data
                list.append(stress_percentage, 50)
                list.append(essentials, 12556)
                list.append(non_essentials, 12556)
                list.append(amount, 12556)
                # reassigns variables to display on screen
                stress_levels = test_font.render(str(stress_percentage[0]), False, (0, 0, 0))
                amount_left = test_font.render(str(amount[0]), False, (0, 0, 0))
                avg_spending_essential = test_font.render(str(essentials[0]), False, (0, 0, 0))
                avg_spending_nonessential = test_font.render(str(non_essentials[0]),
                                                             False, (0, 0, 0))

            # if player hits the downward key
            if event.key == pygame.K_DOWN:
                test_font = pygame.font.Font(None, 27)
                text_surface = test_font.render(' ', False, (0, 0, 0))
                text_surface2 = test_font.render('You are a coupled parent. For each scenario, '
                                                 'use LEFT KEY to select FIRST OPTION and use RIGHT'
                                                 ' KEY to select SECOND OPTION [SPACE TO CONTINUE]',
                                                 False, (0, 0, 0))
                parent_coords = (650, 250)
                parent_surface = pygame.transform.scale(pygame.image.load("coupled_parent.jpg"),
                                                        (170, 130))
                test_font = pygame.font.Font(None, 30)
                # data collecting
                list.append(stress_percentage, 50)
                list.append(essentials, 19885)
                list.append(non_essentials, 19885)
                list.append(amount, 19885)
                stress_levels = test_font.render(str(stress_percentage[0]), False, (0, 0, 0))
                amount_left = test_font.render(str(amount[0]), False, (0, 0, 0))
                avg_spending_essential = test_font.render(str(essentials[0]), False, (0, 0, 0))
                avg_spending_nonessential = test_font.render(str(non_essentials[0]), False,
                                                             (0, 0, 0))

            if event.key == pygame.K_SPACE:
                # begins the iteration on the scenarios and rates, then displays it
                text_surface2 = test_font.render(scenarios[scenario_count], False, (0, 0, 0))
                rates = test_font.render(covid_rates[scenario_count], False, (0, 0, 0))

            if event.key == pygame.K_LEFT:
                if scenario_count + 1 in range(len(scenarios)):
                    # break up text for each scenario so we can use value in data aggregation
                    scenario = str.split(scenarios[scenario_count])
                    # displays scenario
                    text_surface2 = test_font.render(scenarios[scenario_count + 1], False,
                                                     (0, 0, 0))

                    # creates value for essential and non-essential lists to align with datasets
                    money_essential = essentials[scenario_count] - int(scenario[12])
                    money_nonessential = non_essentials[scenario_count] + int(scenario[4])
                    new_amount = amount[scenario_count] - int(scenario[4])
                    new_level = stress_percentage[scenario_count] - 5

                    # add those values to the lists for plotting
                    list.append(stress_percentage, new_level)
                    list.append(amount, new_amount)
                    list.append(non_essentials, money_nonessential)
                    list.append(essentials, money_essential)

                    # displays the new values for each value-type shown in game
                    avg_spending_essential = test_font.render(str(money_essential), False,
                                                              (0, 0, 0))
                    avg_spending_nonessential = test_font.render(str(money_nonessential), False,
                                                                 (0, 0, 0))
                    rates = test_font.render(covid_rates[scenario_count + 1], False, (0, 0, 0))
                    amount_left = test_font.render(str(new_amount), False, (0, 0, 0))
                    stress_levels = test_font.render(str(new_level), False, (0, 0, 0))

                    # increase count (index)
                    scenario_count += 1

                    # the conditional will display the analysis of the the data
                    if scenarios[scenario_count] == '[LEFT/RIGHT KEY TO SEE THE GRAPHS]':

                        # reassign coords
                        text_coords = (25, 100)
                        text2_coords = (1010, 100)
                        text_surface = test_font.render('THE CHANGE IN SPENDING BETWEEN INITIAL '
                                                        'MARCH 2020 SPENDING AMOUNT AND '
                                                        'EACH MONTH ', False, (0, 0, 0))
                        house_coords = (2000, 2000)
                        parent_coords = (2000, 2000)

                        # creates and dislays the month headings
                        april = test_font.render('APRIL:', False, (0, 0, 0))
                        may = test_font.render('MAY:', False, (0, 0, 0))
                        june = test_font.render('JUNE:', False, (0, 0, 0))
                        july = test_font.render('JULY:', False, (0, 0, 0))
                        august = test_font.render('AUGUST:', False, (0, 0, 0))
                        september = test_font.render('SEPTEMBER:', False, (0, 0, 0))

                        # creates and displays the essent/non-essent headings
                        ap_essentials = test_font.render('ESSENT: ', False, (0, 0, 0))
                        may_essentials = test_font.render('ESSENT: ', False, (0, 0, 0))
                        july_essentials = test_font.render('ESSENT: ', False, (0, 0, 0))
                        june_essentials = test_font.render('ESSENT: ', False, (0, 0, 0))
                        aug_essentials = test_font.render('ESSENT: ', False, (0, 0, 0))
                        sept_essentials = test_font.render('ESSENT: ', False, (0, 0, 0))

                        ap_nonessentials = test_font.render('NON-ESSENT: ', False, (0, 0, 0))
                        may_nonessentials = test_font.render('NON-ESSENT: ', False, (0, 0, 0))
                        june_nonessentials = test_font.render('NON-ESSENT: ', False, (0, 0, 0))
                        july_nonessentials = test_font.render('NON-ESSENT: ', False, (0, 0, 0))
                        aug_nonessentials = test_font.render('NON-ESSENT: ', False, (0, 0, 0))
                        sept_nonessentials = test_font.render('NON-ESSENT: ', False, (0, 0, 0))

                        # sets changes in essent/non-essent spending by using imported function
                        ma_evalues = change_in_essentials_monthly(essentials)
                        am_evalues = change_in_essentials_monthly(essentials)
                        mj_evalues = change_in_essentials_monthly(essentials)
                        jj_evalues = change_in_essentials_monthly(essentials)
                        ja_evalues = change_in_essentials_monthly(essentials)
                        as_evalues = change_in_essentials_monthly(essentials)

                        ma_nonevalues = change_in_nonessentials_monthly(non_essentials)
                        am_nonevalues = change_in_nonessentials_monthly(non_essentials)
                        mj_nonevalues = change_in_nonessentials_monthly(non_essentials)
                        jj_nonevalues = change_in_nonessentials_monthly(non_essentials)
                        ja_nonevalues = change_in_nonessentials_monthly(non_essentials)
                        as_nonevalues = change_in_nonessentials_monthly(non_essentials)

                        # sets each months essent/non-essent values from previous variables
                        ap_e1 = test_font.render(str(ma_evalues[0]), False, (0, 0, 0))
                        ap_none1 = test_font.render(str(ma_nonevalues[0]), False, (0, 0, 0))
                        may_e1 = test_font.render(str(am_evalues[1]), False, (0, 0, 0))
                        may_none1 = test_font.render(str(am_nonevalues[1]), False, (0, 0, 0))
                        june_e1 = test_font.render(str(mj_evalues[2]), False, (0, 0, 0))
                        june_none1 = test_font.render(str(mj_nonevalues[2]), False, (0, 0, 0))
                        july_e1 = test_font.render(str(jj_evalues[3]), False, (0, 0, 0))
                        july_none1 = test_font.render(str(jj_nonevalues[3]), False, (0, 0, 0))
                        aug_e1 = test_font.render(str(ja_evalues[4]), False, (0, 0, 0))
                        aug_none1 = test_font.render(str(ja_nonevalues[4]), False, (0, 0, 0))
                        sept_e1 = test_font.render(str(as_evalues[5]), False, (0, 0, 0))
                        sept_none1 = test_font.render(str(as_nonevalues[5]), False, (0, 0, 0))

                # conditional created so no error pops up when calling
                # scenarios[scenario_count + 1]
                else:
                    # reassigns coords
                    graph_coords = (720, 120)
                    stress_coords = (790, 490)
                    house_coords = (2000, 2000)
                    text_coords = (420, 100)

                    # titles last screen and opens user's graphs in browser
                    text_surface2 = test_font.render(' ', False, (0, 0, 0))
                    text_surface = test_font.render('YOUR DATA RESULTS (BROWSER) VS. '
                                                    'EXPECTED DATASETS', False, (0, 0, 0))
                    all_graphs(time, essentials, non_essentials, stress_percentage)

            if event.key == pygame.K_RIGHT:
                if scenario_count + 1 in range(len(scenarios)):
                    # break up text for each scenario so we can use value in data aggregation
                    scenario = str.split(scenarios[scenario_count])
                    # displays scenario
                    text_surface2 = test_font.render(str(scenarios[scenario_count + 1]), False,
                                                     (0, 0, 0))

                    # creates value for essential and non-essential lists to align with datasets
                    new_amount = amount[scenario_count] - int(scenario[12])
                    new_level = stress_percentage[scenario_count] + 5
                    money_essential = essentials[scenario_count] + int(scenario[12])
                    money_nonessential = non_essentials[scenario_count] - int(scenario[4])

                    # add those values to the lists for plotting
                    list.append(stress_percentage, new_level)
                    list.append(amount, new_amount)
                    list.append(essentials, money_essential)
                    list.append(non_essentials, money_nonessential)

                    # displays the new values for each value-type shown in game
                    avg_spending_essential = test_font.render(str(money_essential), False,
                                                              (0, 0, 0))
                    avg_spending_nonessential = test_font.render(str(money_nonessential),
                                                                 False, (0, 0, 0))
                    rates = test_font.render(covid_rates[scenario_count + 1], False, (0, 0, 0))
                    amount_left = test_font.render(str(new_amount), False, (0, 0, 0))
                    stress_levels = test_font.render(str(new_level), False, (0, 0, 0))

                    # increase count (index)
                    scenario_count += 1

                    # the conditional will display the analysis of the the data
                    if scenarios[scenario_count] == '[LEFT/RIGHT KEY TO SEE THE GRAPHS]':
                        # reassign coords
                        text_coords = (25, 100)
                        text2_coords = (1010, 100)
                        text_surface = test_font.render('THE CHANGE IN SPENDING BETWEEN INITIAL '
                                                        'MARCH 2020 SPENDING AMOUNT AND '
                                                        'EACH MONTH ', False, (0, 0, 0))
                        house_coords = (2000, 2000)
                        parent_coords = (2000, 2000)

                        # creates and dislays the month headings
                        april = test_font.render('APRIL:', False, (0, 0, 0))
                        may = test_font.render('MAY:', False, (0, 0, 0))
                        june = test_font.render('JUNE:', False, (0, 0, 0))
                        july = test_font.render('JULY:', False, (0, 0, 0))
                        august = test_font.render('AUGUST:', False, (0, 0, 0))
                        september = test_font.render('SEPTEMBER:', False, (0, 0, 0))

                        # creates and displays the essent/non-essent headings
                        ap_essentials = test_font.render('ESSENT: ', False, (0, 0, 0))
                        may_essentials = test_font.render('ESSENT: ', False, (0, 0, 0))
                        july_essentials = test_font.render('ESSENT: ', False, (0, 0, 0))
                        june_essentials = test_font.render('ESSENT: ', False, (0, 0, 0))
                        aug_essentials = test_font.render('ESSENT: ', False, (0, 0, 0))
                        sept_essentials = test_font.render('ESSENT: ', False, (0, 0, 0))

                        ap_nonessentials = test_font.render('NON-ESSENT: ', False, (0, 0, 0))
                        may_nonessentials = test_font.render('NON-ESSENT: ', False, (0, 0, 0))
                        june_nonessentials = test_font.render('NON-ESSENT: ', False, (0, 0, 0))
                        july_nonessentials = test_font.render('NON-ESSENT: ', False, (0, 0, 0))
                        aug_nonessentials = test_font.render('NON-ESSENT: ', False, (0, 0, 0))
                        sept_nonessentials = test_font.render('NON-ESSENT: ', False, (0, 0, 0))

                        # sets changes in essent/non-essent spending by using imported function
                        ma_evalues = change_in_essentials_monthly(essentials)
                        am_evalues = change_in_essentials_monthly(essentials)
                        mj_evalues = change_in_essentials_monthly(essentials)
                        jj_evalues = change_in_essentials_monthly(essentials)
                        ja_evalues = change_in_essentials_monthly(essentials)
                        as_evalues = change_in_essentials_monthly(essentials)

                        ma_nonevalues = change_in_nonessentials_monthly(non_essentials)
                        am_nonevalues = change_in_nonessentials_monthly(non_essentials)
                        mj_nonevalues = change_in_nonessentials_monthly(non_essentials)
                        jj_nonevalues = change_in_nonessentials_monthly(non_essentials)
                        ja_nonevalues = change_in_nonessentials_monthly(non_essentials)
                        as_nonevalues = change_in_nonessentials_monthly(non_essentials)

                        # sets each months essent/non-essent values from previous variables
                        ap_e1 = test_font.render(str(ma_evalues[0]), False, (0, 0, 0))
                        ap_none1 = test_font.render(str(ma_nonevalues[0]), False, (0, 0, 0))
                        may_e1 = test_font.render(str(am_evalues[1]), False, (0, 0, 0))
                        may_none1 = test_font.render(str(am_nonevalues[1]), False, (0, 0, 0))
                        june_e1 = test_font.render(str(mj_evalues[2]), False, (0, 0, 0))
                        june_none1 = test_font.render(str(mj_nonevalues[2]), False, (0, 0, 0))
                        july_e1 = test_font.render(str(jj_evalues[3]), False, (0, 0, 0))
                        july_none1 = test_font.render(str(jj_nonevalues[3]), False, (0, 0, 0))
                        aug_e1 = test_font.render(str(ja_evalues[4]), False, (0, 0, 0))
                        aug_none1 = test_font.render(str(ja_nonevalues[4]), False, (0, 0, 0))
                        sept_e1 = test_font.render(str(as_evalues[5]), False, (0, 0, 0))
                        sept_none1 = test_font.render(str(as_nonevalues[5]), False, (0, 0, 0))

                    # conditional created so no error pops up when calling
                    # scenarios[scenario_count + 1]
                else:
                    # reassigns coords
                    graph_coords = (720, 120)
                    stress_coords = (790, 490)
                    house_coords = (2000, 2000)
                    text_coords = (420, 100)

                    # titles last screen and opens user's graphs in browser
                    text_surface2 = test_font.render(' ', False, (0, 0, 0))
                    text_surface = test_font.render('YOUR DATA RESULTS (BROWSER) VS. '
                                                    'EXPECTED DATASETS', False, (0, 0, 0))
                    all_graphs(time, essentials, non_essentials, stress_percentage)

    # display these texts before any event occurs (any button is pressed)
    screen.blit(pygame.transform.scale(background_surface, (1500, 1000)), (0, -200))
    screen.blit(pygame.transform.scale(house_surface, (1500, 1000)), house_coords)
    screen.blit(parent_surface, parent_coords)
    screen.blit(stress, stress_coords)
    screen.blit(graph, graph_coords)
    screen.blit(april, (50, 150))
    screen.blit(may, (50, 350))
    screen.blit(june, (50, 550))
    screen.blit(july, (450, 150))
    screen.blit(august, (450, 350))
    screen.blit(september, (450, 550))
    screen.blit(ap_essentials, (60, 200))
    screen.blit(ap_nonessentials, (60, 250))
    screen.blit(may_essentials, (60, 400))
    screen.blit(may_nonessentials, (60, 450))
    screen.blit(july_essentials, (60, 600))
    screen.blit(june_nonessentials, (60, 650))
    screen.blit(june_essentials, (460, 200))
    screen.blit(july_nonessentials, (460, 250))
    screen.blit(aug_essentials, (460, 400))
    screen.blit(aug_nonessentials, (460, 450))
    screen.blit(sept_essentials, (460, 600))
    screen.blit(sept_nonessentials, (460, 650))
    screen.blit(ap_e1, (155, 200))
    screen.blit(ap_none1, (205, 250))
    screen.blit(may_e1, (155, 400))
    screen.blit(may_none1, (205, 450))
    screen.blit(june_e1, (155, 600))
    screen.blit(june_none1, (205, 650))
    screen.blit(july_e1, (555, 200))
    screen.blit(july_none1, (605, 250))
    screen.blit(aug_e1, (555, 400))
    screen.blit(aug_none1, (605, 450))
    screen.blit(sept_e1, (555, 600))
    screen.blit(sept_none1, (605, 650))
    screen.blit(text_surface, text_coords)
    screen.blit(text_surface2, text2_coords)
    screen.blit(test_font.render(' ESSENTIAL SPENDING: $', False, (0, 0, 0)), (15, 25))
    screen.blit(test_font.render(' NON-ESSENTIAL SPENDING: $', False, (0, 0, 0)), (15, 55))
    screen.blit(test_font.render(' AMOUNT LEFT: $', False, (0, 0, 0)), (1150, 25))
    screen.blit(test_font.render(' STRESS PERCENTAGE: ', False, (0, 0, 0)), (1150, 55))
    screen.blit(stress_levels, (1388, 55))
    screen.blit(amount_left, (1325, 25))
    screen.blit(avg_spending_essential, (275, 25))
    screen.blit(avg_spending_nonessential, (325, 55))
    screen.blit(rates, (50, 150))

    # updates the game for each iteration in while loop
    pygame.display.update()
