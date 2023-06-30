from data_func.apps_data_stat import *
from data_func.apps_data_vis import *


def tests() -> None:
    """
    Почти нет смысла pytest т.к. датасет может меняться.
    Корректность графиков нужно контролировать визуально.
    """
    get_data_overview()
    get_all_categories()
    get_all_genres()
    get_mean_rating_size_price_installs()
    get_median_rating_size_price_installs()
    get_x_most_popular_genres()
    get_x_most_popular_apps()
    visualize_categories()
    visualize_genres()
    visualize_rating_per_genre()
    visualize_rating_as_boxenplot()
    visualize_size_per_genre()
    visualize_free_and_paid_per_genre()
    visualize_price_as_scatterplot()
    visualize_installs_per_genre()
    visualize_optimal_app_size_per_genre()
