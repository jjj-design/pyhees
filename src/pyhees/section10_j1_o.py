# ヘアドライヤー

def get_E_Elc_dryer_d_t(P_Elc_dryer_rtd, t_dryer_oprt_d_t, number_of_people):
    """時刻別消費電力量を計算する

    Parameters
    ----------
    P_Elc_dryer_rtd : float
        定格消費電力, W

    t_dryer_oprt_d_t : ndarray(N-dimensional array)
        1年間の全時間の使用時間を格納したND配列, h
        d日t時の使用時間が年開始時から8760個連続して格納されている

    number_of_people : int
        世帯人数, 人        

    Returns
    ----------
    E_Elc_dryer_d_t : ndarray(N-dimensional array)
        1年間の全時間の消費電力量を格納したND配列, kWh
        d日t時の消費電力量が年開始時から8760個連続して格納されている
    """

    P_Elc_dryer_oprt = get_P_Elc_dryer_oprt(P_Elc_dryer_rtd, number_of_people)

    E_Elc_dryer_d_t = P_Elc_dryer_oprt * t_dryer_oprt_d_t
    E_Elc_dryer_d_t = E_Elc_dryer_d_t * 10**(-3)

    return E_Elc_dryer_d_t


def get_P_Elc_dryer_oprt(P_Elc_dryer_rtd, number_of_people):
    """使用時の消費電力を計算する

    Parameters
    ----------
    P_Elc_dryer_rtd : float
        定格消費電力, W

    number_of_people : int
        世帯人数, 人        

    Returns
    ----------
    P_Elc_dryer_oprt : float
        使用時の消費電力, W
    """

    if number_of_people == 4:
        P_Elc_dryer_oprt = 0.8974 * P_Elc_dryer_rtd
    elif number_of_people == 3:
        P_Elc_dryer_oprt = 0.8974 * P_Elc_dryer_rtd * 3 / 3
    elif number_of_people == 2:
        P_Elc_dryer_oprt = 0.8974 * P_Elc_dryer_rtd * 2 / 3
    elif number_of_people == 1:
        P_Elc_dryer_oprt = 0.8974 * P_Elc_dryer_rtd * 1 / 3
    else:
        raise ValueError(number_of_people)

    return P_Elc_dryer_oprt
