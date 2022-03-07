# MDコンポ

def get_E_Elc_audio_microsystem_with_md_d_t( \
        P_Elc_audio_microsystem_with_md_rtd, \
        P_Elc_audio_microsystem_with_md_standby_rtd, \
        t_audio_microsystem_with_md_listening_d_t, \
        t_audio_microsystem_with_md_standby_d_t):
    """時刻別消費電力量を計算する
    
    Parameters
    ----------
    P_Elc_audio_microsystem_with_md_rtd : float
        定格消費電力, W
        
    P_Elc_audio_microsystem_with_md_standby_rtd : float
        待機時の定格消費電力, W
        
    t_audio_microsystem_with_md_listening_d_t : ndarray(N-dimensional array)
        1年間の全時間の聴取時間を格納したND配列, h
        d日t時の聴取時間が年開始時から8760個連続して格納されている
    
    t_audio_microsystem_with_md_standby_d_t : ndarray(N-dimensional array)
        1年間の全時間の待機時間を格納したND配列, h
        d日t時の待機時間が年開始時から8760個連続して格納されている

    Returns
    ----------
    E_Elc_audio_microsystem_with_md_d_t : ndarray(N-dimensional array)
        1年間の全時間の消費電力量を格納したND配列, Wh
        d日t時の消費電力量が年開始時から8760個連続して格納されている
    """
    
    P_Elc_audio_microsystem_with_md_listening = get_P_Elc_audio_microsystem_with_md_listening(P_Elc_audio_microsystem_with_md_rtd)
    P_Elc_audio_microsystem_with_md_standby = get_P_Elc_audio_microsystem_with_md_standby(P_Elc_audio_microsystem_with_md_standby_rtd)
    
    E_Elc_audio_microsystem_with_md_d_t \
        = P_Elc_audio_microsystem_with_md_listening * t_audio_microsystem_with_md_listening_d_t \
        + P_Elc_audio_microsystem_with_md_standby * t_audio_microsystem_with_md_standby_d_t
        
    E_Elc_audio_microsystem_with_md_d_t = E_Elc_audio_microsystem_with_md_d_t * 10**(-3)
    
    return E_Elc_audio_microsystem_with_md_d_t



def get_P_Elc_audio_microsystem_with_md_listening(P_Elc_audio_microsystem_with_md_rtd):
    """聴取時の消費電力を計算する
    
    Parameters
    ----------
    P_Elc_audio_microsystem_with_md_rtd : float
        定格消費電力, W

    Returns
    ----------
    P_Elc_audio_microsystem_with_md_listening : float
        聴取時消費電力, W
    """
        
    P_Elc_audio_microsystem_with_md_listening = \
        0.4 * P_Elc_audio_microsystem_with_md_rtd
        
    return P_Elc_audio_microsystem_with_md_listening



def get_P_Elc_audio_microsystem_with_md_standby(P_Elc_audio_microsystem_with_md_standby_rtd):
    """待機時の消費電力を計算する
    
    Parameters
    ----------
    P_Elc_audio_microsystem_with_md_standby_rtd : float
        定格消費電力, W

    Returns
    ----------
    P_Elc_audio_microsystem_with_md_standby : float
        聴取時消費電力, W
    """
        
    P_Elc_audio_microsystem_with_md_standby = \
        P_Elc_audio_microsystem_with_md_standby_rtd
        
    return P_Elc_audio_microsystem_with_md_standby

