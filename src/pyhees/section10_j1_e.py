# 電気ケトル

def get_E_Elc_kttl_d_t(P_Elc_kttl_boil_rtd, tm_kttl_boil_d_t, number_of_people):
    """時刻別の消費電力を計算する
    
    Parameters
    ----------
    P_Elc_kttl_boil_rtd : float
        定格消費電力,W
        
    number_of_people : int
        世帯人数, 人
        
    Returns
    ----------
    E_Elc_kttl_d_t : ndarray(N-dimensional array)
        1年間の全時間の消費電力量を格納したND配列, Wh
        d日t時の消費電力量が年開始時から8760個連続して格納されている
    """
    
    E_Elc_kttl_boil = get_E_Elc_kttl_boil(P_Elc_kttl_boil_rtd)
    
    if number_of_people == 4:
        E_Elc_kttl_d_t = E_Elc_kttl_boil * tm_kttl_boil_d_t / 1000
    elif number_of_people == 3:
        E_Elc_kttl_d_t = E_Elc_kttl_boil * tm_kttl_boil_d_t * 3 / 3 / 1000
    elif number_of_people == 2:
        E_Elc_kttl_d_t = E_Elc_kttl_boil * tm_kttl_boil_d_t * 2 / 3 / 1000
    elif number_of_people == 1:
        E_Elc_kttl_d_t = E_Elc_kttl_boil * tm_kttl_boil_d_t * 1 / 3 / 1000
    else:
        raise ValueError(number_of_people)
        
    return E_Elc_kttl_d_t


def get_E_Elc_kttl_boil(P_Elc_kttl_boil_rtd):
    """沸き上げ時の消費電力量を計算する
    
    Parameters
    ----------
    P_Elc_kttl_boil_rtd : float
        定格消費電力,W
        
    Returns
    ----------
    E_Elc_kttl_boil : float
        1回の沸き上げ消費電力量,Wh
    """

    E_Elc_kttl_boil = P_Elc_kttl_boil_rtd * 0.1

        
    return E_Elc_kttl_boil


