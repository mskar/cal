# %% [markdown]
# ---
# title: Weekly and Pently Schedule Comparison
# author: Martin Laptev
# date: now
# date-format: x
# filters:
#   - date.lua
# ---

# %%
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe

plt.rcParams.update(
    {
        "legend.fontsize": "x-large",
        "axes.labelsize": "x-large",
        "axes.titlesize": "xx-large",
        "xtick.labelsize" : "large",
        "ytick.labelsize" : "large",
        'figure.dpi': 300,
        'figure.figsize': [6, 4],
    }
)

# %%
# | tags: [fig-schedules]
# | label: fig-schedules
# | fig-cap: "Weekly schedule and Schedule 3 comparison"
# | fig-cap-location: margin
# | fig-subcap:
# |   - "Proportion of the day spent working and resting every day of the week"
# |   - "Proportion of the day spent working and resting every day of the pent"
# | fig-alt:
# |   - "Bar chart showing work in red and rest in blue across 7 days"
# |   - "Bar chart showing work in red and rest in blue across 5 days"
# | layout-ncol: 2
import pandas as pd

ax = (
    pd.DataFrame(
        {
            "Days": ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"],
            "Morning rest": [3 / 8] * 5 + [1] * 2,
            "Work": [1 / 3] * 5 + [0] * 2,
            "Evening rest": [7 / 24] * 5 + [0] * 2,
        }
    )
    .set_index("Days")
    .plot.bar(
        stacked=True,
        color=["#377eb8", "#e41a1c", "#377eb8"],
        title="Weekly schedule",
        legend=False,
        xlabel="Days of the week",
        ylabel="Proportion of the day",
        rot=0,
        width=0.8,
    )
)
ax.invert_yaxis()
ax.legend(["Rest", "Work"], loc="upper right")
ax.patch.set_alpha(0)

for c in ax.containers:
    labels = [round(v.get_height(), 3) if v.get_height() > 0 else "" for v in c]
    labels = [str(l)[1:] for l in labels if l != 1]
    ax.bar_label(c, labels=labels, label_type="center", color="black", path_effects=[pe.withStroke(linewidth=3, foreground="white")], fontsize=15)

ax = (
    pd.DataFrame(
        {
            "Days": ["0 or 5", "1 or 6", "2 or 7", "3 or 8", "4 or 9"],
            "Morning rest": [0.3] * 3 + [1] * 2,
            "Work": [0.4] * 3 + [0] * 2,
            "Evening rest": [0.3] * 3 + [0] * 2,
        }
    )
    .set_index("Days")
    .plot.bar(
        stacked=True,
        color=["#377eb8", "#e41a1c", "#377eb8"],
        title="Schedule 3",
        legend=False,
        xlabel="Days of the dek",
        ylabel="Proportion of the day",
        rot=0,
        width=0.8,
    )
)
ax.invert_yaxis()
ax.legend(["Rest", "Work"], loc="upper right")
ax.patch.set_alpha(0)

for c in ax.containers[:-1]:
    labels = [round(v.get_height(), 1) if v.get_height() > 0 else "" for v in c]
    labels = [str(l)[1:] for l in labels if l != 1]
    ax.bar_label(c, labels=labels, label_type="center", color="black", path_effects=[pe.withStroke(linewidth=3, foreground="white")], fontsize=18)
