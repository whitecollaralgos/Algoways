"""
Mapping utilities for Dhan broker integration.
Provides exchange code mappings between AlgoWays and Dhan formats.
"""
from typing import Dict

# Exchange code mappings
# AlgoWays exchange code -> Dhan exchange code
OPENALGO_TO_DHAN_EXCHANGE = {
    "NSE": "NSE_EQ",
    "BSE": "BSE_EQ",
    "NFO": "NSE_FNO",
    "BFO": "BSE_FNO",
    "CDS": "NSE_CURRENCY",
    "BCD": "BSE_CURRENCY",
    "MCX": "MCX_COMM",
    "NSE_INDEX": "IDX_I",
    "BSE_INDEX": "IDX_I"
}

# Dhan exchange code -> AlgoWays exchange code
DHAN_TO_OPENALGO_EXCHANGE = {v: k for k, v in OPENALGO_TO_DHAN_EXCHANGE.items()}

def get_dhan_exchange(algoways_exchange: str) -> str:
    """
    Convert AlgoWays exchange code to Dhan exchange code.
    
    Args:
        algoways_exchange (str): Exchange code in AlgoWays format
        
    Returns:
        str: Exchange code in Dhan format
    """
    return OPENALGO_TO_DHAN_EXCHANGE.get(algoways_exchange, algoways_exchange)
    
def get_algoways_exchange(dhan_exchange: str) -> str:
    """
    Convert Dhan exchange code to AlgoWays exchange code.
    
    Args:
        dhan_exchange (str): Exchange code in Dhan format
        
    Returns:
        str: Exchange code in AlgoWays format
    """
    return DHAN_TO_OPENALGO_EXCHANGE.get(dhan_exchange, dhan_exchange)
