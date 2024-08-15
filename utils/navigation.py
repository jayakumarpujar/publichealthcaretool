from views import main_menu, hazard_data, analysis_data
from views import baseline_data_main


def navigate(page):
    if page == "Main Menu":
        main_menu.show()
    elif page == "Baseline Data":
        baseline_data_main.show()
    elif page == "Hazard Data":
        hazard_data.show()
    elif page == "Analysis Data":
        analysis_data.show()
