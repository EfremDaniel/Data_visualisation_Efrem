
from matplotlib.ticker import FuncFormatter
def horizontal_bar_option(ax, **options):

    print(options.get("title"))
    
    ax.set_title(options.get("title", ""), loc="left")
    ax.set_xlabel(options.get("xlabel", ""), loc="left")
    ax.set_ylabel(options.get("ylabel", ""), rotation=0)
    ax.yaxis.set_label_coords(
        options.get("ylabel_x_coord", -0.1), options.get("ylabel_x_coord", 1))
   
    ax.legend().remove()
    ax.invert_yaxis()

    return ax

def save_fig_from_ax(ax, save_path):
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(save_path)

def thousands_formatter(ax, axis="x"):
    formatter = FuncFormatter(
        lambda val, pos: f"{int(val/1000)}K" if val else f"{val:.0f}"
    )
    if axis == "x":
        ax.xaxis.set_major_formatter(formatter)
    elif axis == "y":
        ax.yaxis.set_major_formatter(formatter)
    elif axis == "both":
        ax.xaxis.set_major_formatter(formatter)
        ax.yaxis.set_major_formatter(formatter)

    return ax


def save_fig_from_ax(ax, **options):
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(options.get("save_path", ""), dpi=options.get("dpi", 300))