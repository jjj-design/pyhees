# 液晶テレビ

def get_E_Elc_tv_led_d_t(P_Elc_tv_led_standby_rtd, P_Elc_tv_led_view_rtd, t_tv_led_lv_standby_d_t, t_tv_led_lv_view_d_t, t_tv_led_standby_d_t, t_tv_led_view_d_t, number_of_people):
    """時刻別消費電力量を計算する
    
    Parameters
    ----------
    P_Elc_tv_led_standby_rtd : float
        定格待機電力, W
        
    P_Elc_tv_led_view_rtd : float
        定格視聴電力, W
        
    t_tv_led_lv_standby_d_t : ndarray(N-dimensional array)
        居間に設置されたテレビの1年間の全時間の待機時間を格納したND配列, h
        d日t時の待機時間が年開始時から8760個連続して格納されている

    t_tv_led_lv_view_d_t : ndarray(N-dimensional array)
        居間に設置されたテレビの1年間の全時間の視聴時間を格納したND配列, h
        d日t時の視聴時間が年開始時から8760個連続して格納されている

    t_tv_led_standby_d_t : ndarray(N-dimensional array)
        居間以外に設置されたテレビの1年間の全時間の待機時間を格納したND配列, h
        d日t時の待機時間が年開始時から8760個連続して格納されている

    t_tv_led_view_d_t : ndarray(N-dimensional array)
        居間以外に設置されたテレビの1年間の全時間の視聴時間を格納したND配列, h
        d日t時の視聴時間が年開始時から8760個連続して格納されている
    
    number_of_people : int
        世帯人数, 人
        
    Returns
    ----------
    E_Elc_tv_led_d_t : ndarray(N-dimensional array)
        1年間の全時間の消費電力量を格納したND配列, Wh
        d日t時の消費電力量が年開始時から8760個連続して格納されている
    """
    
    P_Elc_tv_led_standby = get_P_Elc_tv_led_standby(P_Elc_tv_led_standby_rtd, number_of_people, True)
    P_Elc_tv_led_view = get_P_Elc_tv_led_view(P_Elc_tv_led_view_rtd, number_of_people, True)
    E_Elc_tv_led_lv_d_t = P_Elc_tv_led_standby * t_tv_led_lv_standby_d_t + P_Elc_tv_led_view * t_tv_led_lv_view_d_t
    
    P_Elc_tv_led_standby = get_P_Elc_tv_led_standby(P_Elc_tv_led_standby_rtd, number_of_people, False)
    P_Elc_tv_led_view = get_P_Elc_tv_led_view(P_Elc_tv_led_view_rtd, number_of_people, False)
    E_Elc_tv_led_nlv_d_t = P_Elc_tv_led_standby * t_tv_led_standby_d_t + P_Elc_tv_led_view * t_tv_led_view_d_t
    
    E_Elc_tv_led_d_t = (E_Elc_tv_led_lv_d_t + E_Elc_tv_led_nlv_d_t) * 10**(-3)
    
    return E_Elc_tv_led_d_t


def get_P_Elc_tv_led_standby(P_Elc_tv_led_standby_rtd, number_of_people, in_a_living_room):
    """待機時の消費電力を計算する
    
    Parameters
    ----------
    P_Elc_tv_led_standby_rtd : float
        定格待機電力, W
        
    number_of_people : int
        世帯人数, 人

    in_a_living_room: Boolean
        設置場所が居間である, 真偽値　True：参照スケジュールは「居間」, False：参照スケジュールは「洋室1」
        
    Returns
    ----------
    P_Elc_tv_led_standby : float
        待機電力, W
    """
    
    if in_a_living_room:
        P_Elc_tv_led_standby = P_Elc_tv_led_standby_rtd
    else:
        P_Elc_tv_led_standby = P_Elc_tv_led_standby_rtd * 0.367 / 0.15
    
    if number_of_people == 4:
        P_Elc_tv_led_standby = P_Elc_tv_led_standby
    elif number_of_people == 3:
        P_Elc_tv_led_standby = P_Elc_tv_led_standby * 3 / 3
    elif number_of_people == 2:
        P_Elc_tv_led_standby = P_Elc_tv_led_standby * 2 / 3
    elif number_of_people == 1:
        P_Elc_tv_led_standby = P_Elc_tv_led_standby * 1 / 3
    else:
        raise ValueError(number_of_people)
        
    return P_Elc_tv_led_standby


def get_P_Elc_tv_led_view(P_Elc_tv_led_view_rtd, number_of_people, in_a_living_room):
    """視聴時の消費電力を計算する
    
    Parameters
    ----------
    P_Elc_tv_led_view_rtd : float
        定格視聴電力, W
        
    number_of_people : int
        世帯人数, 人
        
    in_a_living_room: Boolean
        設置場所が居間である, 真偽値　True：参照スケジュールは「居間」, False：参照スケジュールは「洋室1」
        
    Returns
    ----------
    P_Elc_tv_led_view : float
        視聴電力, W
    """

    
    if in_a_living_room:
        P_Elc_tv_led_view = P_Elc_tv_led_view_rtd
    else:
        P_Elc_tv_led_view = P_Elc_tv_led_view_rtd * 63 / 125
    
    if number_of_people == 4:
        P_Elc_tv_led_view = 0.8579 * P_Elc_tv_led_view
    elif number_of_people == 3:
        P_Elc_tv_led_view = 0.8579 * P_Elc_tv_led_view * 3 / 3    
    elif number_of_people == 2:
        P_Elc_tv_led_view = 0.8579 * P_Elc_tv_led_view * 2 / 3
    elif number_of_people == 1:
        P_Elc_tv_led_view = 0.8579 * P_Elc_tv_led_view * 1 / 3
    else:
        raise ValueError(number_of_people)
        
        
        
    return P_Elc_tv_led_view


if __name__ == "__main__":
    from pyhees.section11_1 import load_outdoor, get_Theta_ex, get_Theta_ex_d_Ave_d

    region = 6
    outdoor = load_outdoor()
    Theta_ex_d_t = get_Theta_ex(region, outdoor)
    Theta_ex_d_Ave_d = get_Theta_ex_d_Ave_d(Theta_ex_d_t)

    E_Elc_rfrg_d_t = get_E_Elc_rfrg_d_t(150, 0.9, Theta_ex_d_Ave_d, 330, 2006)
    print(sum(E_Elc_rfrg_d_t))