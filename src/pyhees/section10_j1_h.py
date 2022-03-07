# パソコン

def get_E_Elc_PC_d_t(P_Elc_PC_rtd, t_PC_oprt_d_t):
    """時刻別消費電力量を計算する

    Parameters
    ----------
    P_Elc_PC_rtd : float
        定格消費電力, W

    t_PC_oprt_d_t : ndarray(N-dimensional array)
        1年間の全時間の使用時間を格納したND配列, h
        d日t時の使用時間が年開始時から8760個連続して格納されている

    Returns
    ----------
    E_Elc_PC_d_t : ndarray(N-dimensional array)
        1年間の全時間の消費電力量を格納したND配列, kWh
        d日t時の消費電力量が年開始時から8760個連続して格納されている
    """

    P_Elc_PC_oprt = get_P_Elc_PC_oprt(P_Elc_PC_rtd)

    E_Elc_PC_oprt_d_t = P_Elc_PC_oprt * t_PC_oprt_d_t
    E_Elc_PC_oprt_d_t = E_Elc_PC_oprt_d_t * 10**(-3)

    return E_Elc_PC_oprt_d_t


def get_P_Elc_PC_oprt(P_Elc_PC_rtd):
    """使用時の消費電力を計算する

    Parameters
    ----------
    P_Elc_PC_rtd : float
        定格消費電力, W

    Returns
    ----------
    P_Elc_PC_oprt : float
        使用時の消費電力, W
    """

    P_Elc_PC_oprt = 1.0871 * P_Elc_PC_rtd + 2.2719

    return P_Elc_PC_oprt
