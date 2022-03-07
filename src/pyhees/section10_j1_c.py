# 便座

def get_E_Elc_toilet_seat_heater_d_t(theta_ave_d, P_Elc_toilet_seat_heater_rtd, t_toilet_seat_heater_d_t):
    """時刻別消費電力量を計算する
    
    Parameters
    ----------
    theta_ave_d : float
        日付dにおける平均外気温度（地域、季節によらず　11.23）, ℃

    P_Elc_toilet_seat_heater_rtd : float
        便座暖房時の定格消費電力, W
        
    t_toilet_seat_heater_d_t : ndarray(N-dimensional array)
        1年間の全時間の暖房時間を格納したND配列, h
        d日t時の暖房時間が年開始時から8760個連続して格納されている
    
    Returns
    ----------
    E_Elc_toilet_seat_heater_d_t : ndarray(N-dimensional array)
        1年間の全時間の消費電力量を格納したND配列, Wh
        d日t時の消費電力量が年開始時から8760個連続して格納されている
    """
    
    P_Elc_toilet_seat_heater = get_P_Elc_toilet_seat_heater(theta_ave_d, P_Elc_toilet_seat_heater_rtd)
    
    E_Elc_toilet_seat_heater_d_t = P_Elc_toilet_seat_heater * t_toilet_seat_heater_d_t
    E_Elc_toilet_seat_heater_d_t = E_Elc_toilet_seat_heater_d_t * 10**(-3)
    
    return E_Elc_toilet_seat_heater_d_t


def get_P_Elc_toilet_seat_heater(theta_ave_d, P_Elc_toilet_seat_heater_rtd):
    """暖房時の消費電力を計算する
    
    Parameters
    ----------
    theta_ave_d : float
        日付dにおける平均外気温度（地域、季節によらず　11.23）, ℃

    P_Elc_toilet_seat_heater_rtd : float
        便座暖房時の定格消費電力, W
        
    Returns
    ----------
    P_Elc_toilet_seat_heater : float
        便座暖房時の消費電力, W
    """
    theata_toilet_ave_d = 0.4984 * theta_ave_d + 13.427
    
    
    # E_Elc_toilet_seat_heater_d = -20.01 * theata_toilet_ave_d \
    #                            + 922.4 * P_Elc_toilet_seat_heater_rtd / 45
    
    E_Elc_toilet_seat_heater_d = -20.1 * theata_toilet_ave_d \
                               + 922.4 * P_Elc_toilet_seat_heater_rtd / 45
    
    P_Elc_toilet_seat_heater = E_Elc_toilet_seat_heater_d / (24 * 1)

        
    return P_Elc_toilet_seat_heater

