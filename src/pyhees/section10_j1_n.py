# 電気スタンド


def get_E_Elc_desk_lamp_d_t(P_Elc_desk_lamp_rtd, t_desk_lamp_oprt_d_t):
    """時刻別消費電力量を計算する

    Parameters
    ----------
    P_Elc_desk_lamp_rtd : float
        定格消費電力, W

    t_desk_lamp_oprt_d_t : ndarray(N-dimensional array)
        1年間の全時間の点灯時間を格納したND配列, h
        d日t時の点灯時間が年開始時から8760個連続して格納されている

    Returns
    ----------
    E_Elc_desk_lamp_d_t : ndarray(N-dimensional array)
        1年間の全時間の消費電力量を格納したND配列, kWh
        d日t時の消費電力量が年開始時から8760個連続して格納されている
    """

    P_Elc_desk_lamp_oprt = get_P_Elc_desk_lamp_oprt(P_Elc_desk_lamp_rtd)

    E_Elc_desk_lamp_d_t = P_Elc_desk_lamp_oprt * t_desk_lamp_oprt_d_t
    E_Elc_desk_lamp_d_t = E_Elc_desk_lamp_d_t * 10**(-3)

    return E_Elc_desk_lamp_d_t


def get_P_Elc_desk_lamp_oprt(P_Elc_desk_lamp_rtd):
    """点灯時の消費電力を計算する

    Parameters
    ----------
    P_Elc_desk_lamp_rtd : float
        定格消費電力, W

    Returns
    ----------
    P_Elc_desk_lamp_oprt : float
        使用時の消費電力, W
    """

    P_Elc_desk_lamp_oprt = 1.07 * P_Elc_desk_lamp_rtd

    return P_Elc_desk_lamp_oprt
