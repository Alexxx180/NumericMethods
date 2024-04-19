class SimpsonCalc:
    def __init__():
        self.factor = 2
        self.rows = []

    def __empty_list():
        return [Chars['None'] * 2]

    def blanks(row: list):
        row.extend(__empty__list())
        self.rows.append(row)

    def values(core: SimpsonCore):
        row = __empty_list()
        row.insert(1, Chars['Miss'])
        row.insert(0, core.x)
        row[len(row) - core.i] = core.y
        self.rows.append(row)

    def perform(n: int, core: SimpsonCore, view: SimpsonInterface):
        view.origins(core)
        blanks([core.start, core.yends.start])

        for i in range(1, n):
            core.iteration(i)
            values(core)
            view.line(x, y)

        blanks([core.end, core.yends.end])
        view.output(n)

        return calculate()

