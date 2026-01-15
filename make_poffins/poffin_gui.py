import tkinter as tk
from tkinter import ttk, messagebox
import threading
import queue

# --- Import all backend components ---
from make_poffins.berry.berry_factory import BerryFactory
from make_poffins.berry.berry_filter_interface import *
from make_poffins.berry.berry_sort_and_filter_system import BerrySortAndFilterSystem
from make_poffins.berry.berry_sort_interface import *
from make_poffins.poffin.poffin_cooker import PoffinCooker
from make_poffins.poffin.poffin_factory import PoffinFactory
from make_poffins.poffin.poffin_filter_interface import *
from make_poffins.poffin.poffin_sort_and_filter_system import PoffinSortAndFilterSystem
from make_poffins.poffin.poffin_sort_interface import *
from make_poffins.contest_stats.contest_stats_factory import ContestStatsFactory
from make_poffins.contest_stats.contest_stats_filter_interface import *
from make_poffins.contest_stats.contest_stats_sort_and_filter_system import ContestStatsSortAndFilterSystem
from make_poffins.contest_stats.contest_stats_sort_interface import *
from make_poffins.constants import FLAVORS


class PoffinCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Poffin Recipe Calculator (Advanced)")
        self.root.geometry("650x800")

        style = ttk.Style(self.root)
        style.theme_use("clam")

        self._initialize_variables()
        self.result_queue = queue.Queue()
        self.final_results = []
        self._create_widgets()

    def _initialize_variables(self):
        # Berry Filters
        self.use_berry_any_flavor_lt = tk.BooleanVar()
        self.berry_any_flavor_lt_val = tk.IntVar(value=10)
        self.use_berry_rarity_lt = tk.BooleanVar()
        self.berry_rarity_lt_val = tk.IntVar(value=3)
        self.use_berry_rarity_gt = tk.BooleanVar(value=True)
        self.berry_rarity_gt_val = tk.IntVar(value=11)
        self.use_berry_smoothness_lt = tk.BooleanVar()
        self.berry_smoothness_lt_val = tk.IntVar(value=20)
        self.use_berry_smoothness_gt = tk.BooleanVar()
        self.berry_smoothness_gt_val = tk.IntVar(value=60)
        self.use_berry_main_flavor = tk.BooleanVar()
        self.berry_main_flavor_val = tk.StringVar(value="Spicy")

        # Poffin Filters
        self.use_poffin_level_lt = tk.BooleanVar(value=True)
        self.poffin_level_lt_val = tk.IntVar(value=80)
        self.use_poffin_second_level_lt = tk.BooleanVar()
        self.poffin_second_level_lt_val = tk.IntVar(value=40)
        self.use_poffin_flavors_lt = tk.BooleanVar()
        self.poffin_flavors_lt_val = tk.IntVar(value=2)
        self.use_poffin_flavors_gt = tk.BooleanVar()
        self.poffin_flavors_gt_val = tk.IntVar(value=4)
        self.use_poffin_max_similar = tk.BooleanVar(value=True)
        self.poffin_max_similar_val = tk.IntVar(value=1)
        self.use_poffin_flavor_not_equal = tk.BooleanVar()
        self.poffin_flavor_not_equal_val = tk.StringVar(value="Spicy")

        # Contest Stat Filters
        self.use_stats_rank_lt = tk.BooleanVar()
        self.stats_rank_lt_val = tk.IntVar(value=1)
        self.use_stats_rank_gt = tk.BooleanVar(value=True)
        self.stats_rank_gt_val = tk.IntVar(value=2)
        self.use_stats_eaten_lt = tk.BooleanVar()
        self.stats_eaten_lt_val = tk.IntVar(value=8)
        self.use_stats_eaten_gt = tk.BooleanVar(value=True)
        self.stats_eaten_gt_val = tk.IntVar(value=12)
        self.use_stats_rarity_lt = tk.BooleanVar()
        self.stats_rarity_lt_val = tk.IntVar(value=50)
        self.use_stats_rarity_gt = tk.BooleanVar()
        self.stats_rarity_gt_val = tk.IntVar(value=200)
        self.use_stats_perfect_lt = tk.BooleanVar()
        self.stats_perfect_lt_val = tk.IntVar(value=1)
        self.use_stats_perfect_gt = tk.BooleanVar()
        self.stats_perfect_gt_val = tk.IntVar(value=5)

        # Sorter Variables
        self.berry_primary_sort = tk.StringVar(value="Rarity")
        self.berry_secondary_sort = tk.StringVar(value="Name")
        self.poffin_primary_sort = tk.StringVar(value="Level")
        self.poffin_secondary_sort = tk.StringVar(value="None")
        self.stats_primary_sort = tk.StringVar(value="Rank")
        self.stats_secondary_sort = tk.StringVar(value="Poffins Eaten")

    def _create_widgets(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(expand=True, fill=tk.BOTH)

        notebook = ttk.Notebook(main_frame)
        notebook.pack(expand=True, fill=tk.BOTH, pady=5)

        self.berry_tab = ttk.Frame(notebook)
        self.poffin_tab = ttk.Frame(notebook)
        self.stats_tab = ttk.Frame(notebook)

        notebook.add(self.berry_tab, text="Berries")
        notebook.add(self.poffin_tab, text="Poffins")
        notebook.add(self.stats_tab, text="Contest Stats")

        self._create_berry_tab()
        self._create_poffin_tab()
        self._create_stats_tab()

        action_frame = ttk.Frame(main_frame)
        action_frame.pack(fill=tk.X, pady=(10, 0))

        self.run_button = ttk.Button(
            action_frame, text="Run Calculation", command=self.start_calculation)
        self.run_button.pack(fill=tk.X, ipady=5)

        self.progress = ttk.Progressbar(action_frame, mode='indeterminate')
        self.progress.pack(fill=tk.X, pady=5)

        self.status_label = ttk.Label(action_frame, text="Status: Idle")
        self.status_label.pack(fill=tk.X)

    def _create_scrollable_frame(self, parent):
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(
            parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        return scrollable_frame

    def _create_filter_row(self, parent, use_var, label_text, widget_type, widget_options):
        row_frame = ttk.Frame(parent)
        row_frame.pack(fill=tk.X, pady=2, padx=5)
        ttk.Checkbutton(row_frame, variable=use_var).pack(side=tk.LEFT)
        ttk.Label(row_frame, text=label_text, width=25,
                  anchor="w").pack(side=tk.LEFT, padx=5)
        widget_type(row_frame, **widget_options).pack(side=tk.LEFT,
                                                      fill=tk.X, expand=True)

    def _create_berry_tab(self):
        scroll_frame = self._create_scrollable_frame(self.berry_tab)

        filter_group = ttk.LabelFrame(
            scroll_frame, text="Filters", padding="10")
        filter_group.pack(fill=tk.X, expand=True, pady=5, padx=5)

        self._create_filter_row(filter_group, self.use_berry_any_flavor_lt, "Min Any Flavor >=", ttk.Spinbox, {
                                "from_": 10, "to": 40, "textvariable": self.berry_any_flavor_lt_val})
        self._create_filter_row(filter_group, self.use_berry_rarity_lt, "Min Rarity >=", ttk.Spinbox, {
                                "from_": 1, "to": 60, "textvariable": self.berry_rarity_lt_val})
        self._create_filter_row(filter_group, self.use_berry_rarity_gt, "Max Rarity <=", ttk.Spinbox, {
                                "from_": 1, "to": 60, "textvariable": self.berry_rarity_gt_val})
        self._create_filter_row(filter_group, self.use_berry_smoothness_lt, "Min Smoothness >=", ttk.Spinbox, {
                                "from_": 20, "to": 60, "textvariable": self.berry_smoothness_lt_val})
        self._create_filter_row(filter_group, self.use_berry_smoothness_gt, "Max Smoothness <=", ttk.Spinbox, {
                                "from_": 20, "to": 60, "textvariable": self.berry_smoothness_gt_val})
        self._create_filter_row(filter_group, self.use_berry_main_flavor, "Main Flavor Is", ttk.Combobox, {
                                "textvariable": self.berry_main_flavor_val, "values": FLAVORS, "state": "readonly"})

        sorter_group = ttk.LabelFrame(
            scroll_frame, text="Sorters", padding="10")
        sorter_group.pack(fill=tk.X, expand=True, pady=5, padx=5)

        sorter_options = ["Name", "Rarity", "Smoothness", "Main Flavor Value",
                          "Main Flavor", "Num Flavors", "Weakened Main Flavor Value"]
        ttk.Label(sorter_group, text="Primary Sort:").grid(
            row=0, column=0, sticky="w")
        ttk.Combobox(sorter_group, textvariable=self.berry_primary_sort,
                     values=sorter_options, state="readonly").grid(row=0, column=1, sticky="ew")
        ttk.Label(sorter_group, text="Then By:").grid(
            row=1, column=0, sticky="w")
        ttk.Combobox(sorter_group, textvariable=self.berry_secondary_sort, values=[
                     "None"] + sorter_options, state="readonly").grid(row=1, column=1, sticky="ew")
        sorter_group.columnconfigure(1, weight=1)

    def _create_poffin_tab(self):
        scroll_frame = self._create_scrollable_frame(self.poffin_tab)

        filter_group = ttk.LabelFrame(
            scroll_frame, text="Filters", padding="10")
        filter_group.pack(fill=tk.X, expand=True, pady=5, padx=5)

        self._create_filter_row(filter_group, self.use_poffin_level_lt, "Min Level >=", ttk.Spinbox, {
                                "from_": 0, "to": 200, "textvariable": self.poffin_level_lt_val})
        self._create_filter_row(filter_group, self.use_poffin_second_level_lt, "Min 2nd Level >=", ttk.Spinbox, {
                                "from_": 0, "to": 100, "textvariable": self.poffin_second_level_lt_val})
        self._create_filter_row(filter_group, self.use_poffin_flavors_lt, "Min # Flavors >=", ttk.Spinbox, {
                                "from_": 1, "to": 5, "textvariable": self.poffin_flavors_lt_val})
        self._create_filter_row(filter_group, self.use_poffin_flavors_gt, "Max # Flavors <=", ttk.Spinbox, {
                                "from_": 1, "to": 5, "textvariable": self.poffin_flavors_gt_val})
        self._create_filter_row(filter_group, self.use_poffin_max_similar, "Max Similar <=", ttk.Spinbox, {
                                "from_": 1, "to": 4, "textvariable": self.poffin_max_similar_val})
        self._create_filter_row(filter_group, self.use_poffin_flavor_not_equal, "Main Flavor Is", ttk.Combobox, {
                                "textvariable": self.poffin_flavor_not_equal_val, "values": FLAVORS, "state": "readonly"})

        sorter_group = ttk.LabelFrame(
            scroll_frame, text="Sorters", padding="10")
        sorter_group.pack(fill=tk.X, expand=True, pady=5, padx=5)

        sorter_options = ["Level", "Name", "Smoothness",
                          "Level/Smoothness Ratio", "Rarity"]
        ttk.Label(sorter_group, text="Primary Sort:").grid(
            row=0, column=0, sticky="w")
        ttk.Combobox(sorter_group, textvariable=self.poffin_primary_sort,
                     values=sorter_options, state="readonly").grid(row=0, column=1, sticky="ew")
        ttk.Label(sorter_group, text="Then By:").grid(
            row=1, column=0, sticky="w")
        ttk.Combobox(sorter_group, textvariable=self.poffin_secondary_sort, values=[
                     "None"] + sorter_options, state="readonly").grid(row=1, column=1, sticky="ew")
        sorter_group.columnconfigure(1, weight=1)

    def _create_stats_tab(self):
        scroll_frame = self._create_scrollable_frame(self.stats_tab)

        filter_group = ttk.LabelFrame(
            scroll_frame, text="Filters", padding="10")
        filter_group.pack(fill=tk.X, expand=True, pady=5, padx=5)

        self._create_filter_row(filter_group, self.use_stats_rank_lt, "Min Rank >=", ttk.Spinbox, {
                                "from_": 1, "to": 3, "textvariable": self.stats_rank_lt_val})
        self._create_filter_row(filter_group, self.use_stats_rank_gt, "Max Rank <=", ttk.Spinbox, {
                                "from_": 1, "to": 3, "textvariable": self.stats_rank_gt_val})
        self._create_filter_row(filter_group, self.use_stats_eaten_lt, "Min Poffins Eaten >=", ttk.Spinbox, {
                                "from_": 1, "to": 20, "textvariable": self.stats_eaten_lt_val})
        self._create_filter_row(filter_group, self.use_stats_eaten_gt, "Max Poffins Eaten <=", ttk.Spinbox, {
                                "from_": 1, "to": 20, "textvariable": self.stats_eaten_gt_val})
        self._create_filter_row(filter_group, self.use_stats_rarity_lt, "Min Rarity >=", ttk.Spinbox, {
                                "from_": 1, "to": 200, "textvariable": self.stats_rarity_lt_val})
        self._create_filter_row(filter_group, self.use_stats_rarity_gt, "Max Rarity <=", ttk.Spinbox, {
                                "from_": 1, "to": 200, "textvariable": self.stats_rarity_gt_val})
        self._create_filter_row(filter_group, self.use_stats_perfect_lt, "Min Perfect Values >=", ttk.Spinbox, {
                                "from_": 0, "to": 5, "textvariable": self.stats_perfect_lt_val})
        self._create_filter_row(filter_group, self.use_stats_perfect_gt, "Max Perfect Values <=", ttk.Spinbox, {
                                "from_": 0, "to": 5, "textvariable": self.stats_perfect_gt_val})

        sorter_group = ttk.LabelFrame(
            scroll_frame, text="Sorters", padding="10")
        sorter_group.pack(fill=tk.X, expand=True, pady=5, padx=5)

        sorter_options = ["Rank", "Poffins Eaten", "Rarity", "Unique Berries",
                          "Num Perfect Values", "Coolness", "Beauty", "Cuteness", "Cleverness", "Toughness"]
        ttk.Label(sorter_group, text="Primary Sort:").grid(
            row=0, column=0, sticky="w")
        ttk.Combobox(sorter_group, textvariable=self.stats_primary_sort,
                     values=sorter_options, state="readonly").grid(row=0, column=1, sticky="ew")
        ttk.Label(sorter_group, text="Then By:").grid(
            row=1, column=0, sticky="w")
        ttk.Combobox(sorter_group, textvariable=self.stats_secondary_sort, values=[
                     "None"] + sorter_options, state="readonly").grid(row=1, column=1, sticky="ew")
        sorter_group.columnconfigure(1, weight=1)

    def start_calculation(self):
        self.run_button.config(state="disabled")
        self.status_label.config(text="Status: Assembling rules...")
        self.progress.start()
        self.final_results = []
        threading.Thread(target=self.run_worker, daemon=True).start()
        self.root.after(100, self.process_queue)

    def process_queue(self):
        try:
            message = self.result_queue.get_nowait()
            if isinstance(message, str) and message.startswith("STATUS:"):
                self.status_label.config(text=f"Status: {message[7:]}")
            elif message == "DONE":
                self.progress.stop()
                self.run_button.config(state="normal")
                if self.final_results:
                    self.status_label.config(
                        text=f"Status: Done! Found {len(self.final_results)} results.")
                    self.display_results()
                elif "ERROR:" not in self.status_label.cget("text"):
                    self.status_label.config(text="Status: No results found.")
            elif isinstance(message, str) and message.startswith("ERROR:"):
                self.progress.stop()
                self.run_button.config(state="normal")
                self.status_label.config(text="Status: An error occurred.")
                messagebox.showerror("Calculation Error", message)
                self.final_results = []
            else:
                self.final_results.append(message)
                self.status_label.config(
                    text=f"Status: Found {len(self.final_results)} results...")
            self.root.after(100, self.process_queue)
        except queue.Empty:
            self.root.after(100, self.process_queue)

    def run_worker(self):
        try:
            # --- 1. Berries ---
            self.result_queue.put(
                "STATUS:Applying berry filters and sorters...")
            berry_rules = []
            if self.use_berry_any_flavor_lt.get():
                berry_rules.append(RemoveBerriesWith_AnyFlavorValue_LessThan(
                    self.berry_any_flavor_lt_val.get()))
            if self.use_berry_rarity_lt.get():
                berry_rules.append(RemoveBerriesWith_Rarity_LessThan(
                    self.berry_rarity_lt_val.get()))
            if self.use_berry_rarity_gt.get():
                berry_rules.append(RemoveBerriesWith_Rarity_GreaterThan(
                    self.berry_rarity_gt_val.get()))
            if self.use_berry_smoothness_lt.get():
                berry_rules.append(RemoveBerriesWith_Smoothness_LessThan(
                    self.berry_smoothness_lt_val.get()))
            if self.use_berry_smoothness_gt.get():
                berry_rules.append(RemoveBerriesWith_Smoothness_GreaterThan(
                    self.berry_smoothness_gt_val.get()))
            if self.use_berry_main_flavor.get():
                berry_rules.append(RemoveBerriesWith_MainFlavorName(
                    self.berry_main_flavor_val.get()))

            berry_sorter_map = {"Name": SortBerriesBy_Name, "Rarity": SortBerriesBy_Rarity, "Smoothness": SortBerriesBy_Smoothness, "Main Flavor Value": SortBerriesBy_Main_Flavor_Value,
                                "Main Flavor": SortBerriesBy_Main_Flavor, "Num Flavors": SortBerriesBy_Num_Flavors, "Weakened Main Flavor Value": SortBerriesBy_Weakened_Main_Flavor_Value}
            sec_sort, prim_sort = self.berry_secondary_sort.get(), self.berry_primary_sort.get()
            if sec_sort != "None":
                berry_rules.append(berry_sorter_map[sec_sort]())
            if prim_sort != "None":
                berry_rules.append(berry_sorter_map[prim_sort]())

            berry_system = BerrySortAndFilterSystem(berry_rules)
            berry_factory = BerryFactory(berry_system)
            berry_combinations = berry_factory.get_berry_combinations_4()

            # --- 2. Poffins ---
            self.result_queue.put(
                "STATUS:Applying poffin filters and sorters...")
            poffin_rules = []
            if self.use_poffin_level_lt.get():
                poffin_rules.append(RemovePoffinsWith_Level_LessThan(
                    self.poffin_level_lt_val.get()))
            if self.use_poffin_second_level_lt.get():
                poffin_rules.append(RemovePoffinsWith_SecondLevel_LessThan(
                    self.poffin_second_level_lt_val.get()))
            if self.use_poffin_flavors_lt.get():
                poffin_rules.append(RemovePoffinsWith_NumberOfFlavors_LessThan(
                    self.poffin_flavors_lt_val.get()))
            if self.use_poffin_flavors_gt.get():
                poffin_rules.append(RemovePoffinsWith_NumberOfFlavors_GreaterThan(
                    self.poffin_flavors_gt_val.get()))
            if self.use_poffin_max_similar.get():
                poffin_rules.append(RemovePoffinsWith_MaxNSimilar(
                    self.poffin_max_similar_val.get()))
            if self.use_poffin_flavor_not_equal.get():
                poffin_rules.append(RemovePoffinsWith_Flavor_NotEqual(
                    self.poffin_flavor_not_equal_val.get()))

            poffin_sorter_map = {"Level": SortPoffinsBy_Level, "Name": SortPoffinsBy_Name, "Smoothness": SortPoffinsBy_Smoothness,
                                 "Level/Smoothness Ratio": SortPoffinsBy_LevelToSmoothnessRatioSum}
            sec_sort, prim_sort = self.poffin_secondary_sort.get(), self.poffin_primary_sort.get()
            if sec_sort != "None":
                poffin_rules.append(poffin_sorter_map[sec_sort]())
            if prim_sort != "None":
                poffin_rules.append(poffin_sorter_map[prim_sort]())

            poffin_system = PoffinSortAndFilterSystem(poffin_rules)
            poffin_factory = PoffinFactory(PoffinCooker(
                40), berry_combinations, poffin_system)
            poffin_combos = poffin_factory.get_poffin_permutations_3()

            # --- 3. Contest Stats ---
            self.result_queue.put(
                "STATUS:Applying contest stats filters and sorters...")
            stats_rules = []
            if self.use_stats_rank_lt.get():
                stats_rules.append(RemoveContestStatsWith_Rank_LessThan(
                    self.stats_rank_lt_val.get()))
            if self.use_stats_rank_gt.get():
                stats_rules.append(RemoveContestStatsWith_Rank_GreaterThan(
                    self.stats_rank_gt_val.get()))
            if self.use_stats_eaten_lt.get():
                stats_rules.append(RemoveContestStatsWith_PoffinsEaten_LessThan(
                    self.stats_eaten_lt_val.get()))
            if self.use_stats_eaten_gt.get():
                stats_rules.append(RemoveContestStatsWith_PoffinsEaten_GreaterThan(
                    self.stats_eaten_gt_val.get()))
            if self.use_stats_rarity_lt.get():
                stats_rules.append(RemoveContestStatsWith_Rarity_LessThan(
                    self.stats_rarity_lt_val.get()))
            if self.use_stats_rarity_gt.get():
                stats_rules.append(RemoveContestStatsWith_Rarity_GreaterThan(
                    self.stats_rarity_gt_val.get()))
            if self.use_stats_perfect_lt.get():
                stats_rules.append(RemoveContestStatsWith_NumPerfectValues_LessThan(
                    self.stats_perfect_lt_val.get()))
            if self.use_stats_perfect_gt.get():
                stats_rules.append(RemoveContestStatsWith_NumPerfectValues_GreaterThan(
                    self.stats_perfect_gt_val.get()))

            stats_sorter_map = {"Rank": SortContestStatsBy_Rank, "Poffins Eaten": SortContestStatsBy_PoffinsEaten, "Rarity": SortContestStatsBy_Rarity, "Unique Berries": SortContestStatsBy_NumUniqueBerries, "Num Perfect Values": SortContestStatsBy_NumPerfectValues,
                                "Coolness": SortContestStatsBy_Coolness, "Beauty": SortContestStatsBy_Beauty, "Cuteness": SortContestStatsBy_Cuteness, "Cleverness": SortContestStatsBy_Cleverness, "Toughness": SortContestStatsBy_Toughness}
            sec_sort, prim_sort = self.stats_secondary_sort.get(), self.stats_primary_sort.get()
            if sec_sort != "None":
                stats_rules.append(stats_sorter_map[sec_sort]())
            if prim_sort != "None":
                stats_rules.append(stats_sorter_map[prim_sort]())

            stats_system = ContestStatsSortAndFilterSystem(stats_rules)
            stats_factory = ContestStatsFactory(poffin_combos, stats_system)

            self.result_queue.put(
                "STATUS:Calculating stats (this may take a while)...")
            final_stats = stats_factory.filtered_sorted_contest_stats

            for stat in final_stats:
                self.result_queue.put(stat)

        except Exception as e:
            self.result_queue.put(f"ERROR: {e}")
        finally:
            self.result_queue.put("DONE")

    def display_results(self):
        if not self.final_results:
            messagebox.showinfo(
                "No Results", "No recipes found matching your criteria.")
            return
        res_win = tk.Toplevel(self.root)
        res_win.title("Calculation Results")
        res_win.geometry("900x600")
        cols = ("Rank", "Poffins Eaten", "Rarity", "Unique Berries", "Recipe")
        tree = ttk.Treeview(res_win, columns=cols, show='headings')
        for col in cols:
            tree.heading(
                col, text=col, command=lambda _col=col: self._sort_treeview(tree, _col, False))
            tree.column(col, width=100, anchor="center")
        tree.column("Recipe", width=400, anchor="w")
        for stat in self.final_results:
            if not hasattr(stat, 'poffins'):
                continue
            recipe_str = " | ".join([p.name for p in stat.poffins])
            tree.insert("", "end", values=(stat.rank, stat.poffins_eaten,
                        stat.rarity, stat.unique_berries, recipe_str))
        tree.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar = ttk.Scrollbar(
            res_win, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def _sort_treeview(self, tree, col, reverse):
        data = [(tree.set(item, col), item) for item in tree.get_children('')]
        try:
            data.sort(key=lambda t: int(t[0]), reverse=reverse)
        except ValueError:
            data.sort(reverse=reverse)
        for index, (_, item) in enumerate(data):
            tree.move(item, '', index)
        tree.heading(col, command=lambda: self._sort_treeview(
            tree, col, not reverse))


if __name__ == "__main__":
    root = tk.Tk()
    app = PoffinCalculatorApp(root)
    root.mainloop()
