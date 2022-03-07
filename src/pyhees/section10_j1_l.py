# アイロン


def get_E_Elc_iron_d_t(P_Elc_iron_rtd, t_iron_oprt_d_t):
    """時刻別消費電力量を計算する

    Parameters
    ----------
    P_Elc_iron_rtd : float
        定格消費電力, W

    t_iron_oprt_d_t : ndarray(N-dimensional array)
        1年間の全時間の使用時間を格納したND配列, h
        d日t時の使用時間が年開始時から8760個連続して格納されている

    Returns
    ----------
    E_Elc_iron_d_t : ndarray(N-dimensional array)
        1年間の全時間の消費電力量を格納したND配列, kWh
        d日t時の消費電力量が年開始時から8760個連続して格納されている
    """

    P_Elc_iron_oprt = get_P_Elc_iron_oprt(P_Elc_iron_rtd)

    E_Elc_iron_oprt_d_t = P_Elc_iron_oprt * t_iron_oprt_d_t
    E_Elc_iron_oprt_d_t = E_Elc_iron_oprt_d_t * 10**(-3)

    return E_Elc_iron_oprt_d_t


def get_P_Elc_iron_oprt(P_Elc_iron_rtd):
    """使用時の消費電力を計算する

    Parameters
    ----------
    P_Elc_iron_rtd : float
        定格消費電力, W

    Returns
    ----------
    P_Elc_iron_oprt : float
        使用時の消費電力, W
    """

    P_Elc_iron_oprt = 0.53 * P_Elc_iron_rtd

    return P_Elc_iron_oprt
