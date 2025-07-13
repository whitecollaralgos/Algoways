"""
Zerodha WebSocket streaming module for AlgoWays.

This module provides WebSocket integration with Zerodha's market data streaming API,
following the AlgoWays WebSocket proxy architecture.
"""

from .zerodha_adapter import ZerodhaWebSocketAdapter

__all__ = ['ZerodhaWebSocketAdapter']
