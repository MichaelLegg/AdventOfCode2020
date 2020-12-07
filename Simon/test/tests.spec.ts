import { expect } from "chai";
import { AdventDay } from "../src/common";
import day4 from "../src/day4";
import { calculateSeatId } from "../src/day5";

const IGNORE = Symbol();

type Result = number | typeof IGNORE | Record<string, number>;
type Results = [Result?, Result?];

const tests: {
	[day: number]: {
		sample: Results;
		puzzle: Results;
	};
} = {
	1: {
		sample: [514579, 241861950],
		puzzle: [928896, 295668576],
	},
	2: {
		sample: [2, 1],
		puzzle: [591, 335],
	},
	3: {
		sample: [7, 336],
		puzzle: [207, 2655892800],
	},
	4: {
		sample: [2, { valid: 4, invalid: 0 }],
		puzzle: [208, 167],
	},
	5: {
		sample: [820, IGNORE],
		puzzle: [866, 583],
	},
	6: {
		sample: [11, 6],
		puzzle: [6565, { "": 3137, filtered: 3137 }],
	},
	7: {
		sample: [4],
		puzzle: [248],
	},
};

(async () => {
	for (const day in tests) {
		const mod = (await import("../src/day" + day))
			.default as AdventDay<unknown>;

		describe(`day ${day}`, () => {
			const res = tests[day];

			for (const type of ["sample", "puzzle"]) {
				for (const i of [1, 2]) {
					let val = res[type as keyof typeof res][i - 1];
					if (val === IGNORE || !val) continue;

					if (typeof val === "number") {
						val = { "": val };
					}
					const v = val;
					for (const k in val) {
						const expected = v[k];
						it(`part ${i} ${type} ${k} (${expected})`, async () => {
							const input = await mod.getInput(
								`day${day}.${type === "sample" ? (k || type) + "." : ""}txt`
							);
							const result = mod[("part" + i) as "part1"](
								input,
								k ? k : undefined
							);
							expect(result).to.eq(expected);
						});
					}
				}
			}
		});
	}

	describe("day 5 (binary check)", () => {
		it("part 1 computes seat id correctly", async () => {
			expect(calculateSeatId("FBFBBFFRLR")).to.eq(357);
			expect(calculateSeatId("BFFFBBFRRR")).to.eq(567);
			expect(calculateSeatId("FFFBBBFRRR")).to.eq(119);
			expect(calculateSeatId("BBFFBBFRLL")).to.eq(820);
		});
	});
})();
