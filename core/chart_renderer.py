import os
import mplfinance as mpf
import pandas as pd

class ChartRenderer:
    @staticmethod
    def render_candlestick(data: pd.DataFrame, output_path: str) -> str:
        "candlestick chart renderer"

        abs_path = os.path.abspath(output_path)

        cv_style = mpf.make_mpf_style(
            base_mpf_style='charles',
            gridcolor='none',
            facecolor='white'
        )

        mpf.plot(
            data,
            type='candle',
            style=cv_style,
            savefig=dict(fname=abs_path, dpi=150, bbox_inches='tight', pad_inches=0),
            volume=False,
            axisoff=True,
            show_nontrading=False
        )
        
        return abs_path