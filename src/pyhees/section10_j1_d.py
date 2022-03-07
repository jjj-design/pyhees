# 洗濯機

def get_E_Elc_washer_d_t(E_Elc_washer_wash_rtd, tm_washer_wash_d_t):
    """時刻別消費電力量を計算する
    
    Parameters
    ----------
    E_Elc_washer_wash_rtd : float
        標準コースの洗濯の定格消費電力量,Wh

    tm_washer_wash_d_t : ndarray(N-dimensional array)
        1年間の全時間の洗濯回数を格納したND配列, 回
        d日t時の洗濯回数が年開始時から8760個連続して格納されている
    
    Returns
    ----------
    E_Elc_toilet_seat_heater_d_t : ndarray(N-dimensional array)
        1年間の全時間の消費電力量を格納したND配列, Wh
        d日t時の消費電力量が年開始時から8760個連続して格納されている
    """
    E_Elc_washer_wash = get_E_Elc_washer_wash(E_Elc_washer_wash_rtd) 
    E_Elc_washer_d_t = E_Elc_washer_wash * tm_washer_wash_d_t
    E_Elc_washer_d_t = E_Elc_washer_d_t * 10**(-3)
    
    return E_Elc_washer_d_t


def get_E_Elc_washer_wash(E_Elc_washer_wash_rtd):
    """洗濯時の消費電力量を計算する
    
    Parameters
    ----------
    E_Elc_washer_wash_rtd : float
        標準コースの洗濯の定格消費電力量,Wh
        
    Returns
    ----------
    E_Elc_washer_wash : float
        1回の洗濯の消費電力量,Wh
    """

    E_Elc_washer_wash = 1.3503 * E_Elc_washer_wash_rtd - 42.848

        
    return E_Elc_washer_wash

