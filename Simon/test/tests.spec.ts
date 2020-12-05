import { expect } from "chai";
import { AdventDay } from "../src/common";
import day4 from "../src/day4";
import { calculateSeatId } from "../src/day5";

const IGNORE = Symbol();

const tests: {
	[day: number]: {
		sample1?: any;
		1?: any;
		sample2?: any;
		2?: any;
	};
} = {
	1: {
		sample1: 514579,
		1: 928896,
		sample2: 241861950,
		2: 295668576,
	},
	2: {
		sample1: 2,
		1: 591,
		sample2: 1,
		2: 335,
	},
	3: {
		sample1: 7,
		1: 207,
		sample2: 336,
		2: 2655892800,
	},
	4: {
		sample1: 2,
		1: 208,
		sample2: IGNORE,
		2: 167,
	},
	5: {
		sample1: 820,
		1: 866
	},
};

(async () => {
	for (const day in tests) {
		const mod = (await import("../src/day" + day))
			.default as AdventDay<unknown>;

		describe(`day ${day}`, () => {
			const res = tests[day];

			for (const type of ["sample", ""]) {
				for (const part of [1, 2]) {
					const expected = res[(type + part) as keyof typeof res];
					if (expected !== IGNORE) {
						it(`part ${part} using ${type || "puzzle"} data`, async () => {
							const result = mod[("part" + part) as "part1"](
								await mod.getInput(`day${day}.${type}${type ? "." : ""}txt`)
							);
							expect(result).to.eq(expected);
						});
					}
				}
			}
		});
	}

	describe("day 4 (extra samples)", () => {
		it("part 2 using sample invalid data", async () => {
			expect(day4.part2(await day4.getInput("day4.invalid.txt"))).to.eq(0);
		});
		it("part 2 using sample valid data", async () => {
			expect(day4.part2(await day4.getInput("day4.valid.txt"))).to.eq(4);
		});
	});

	describe("day 5 (binary check)", () => {
		it("part 1 computes seat id correctly", async () => {
			expect(calculateSeatId("FBFBBFFRLR")).to.eq(357);
			expect(calculateSeatId("BFFFBBFRRR")).to.eq(567);
			expect(calculateSeatId("FFFBBBFRRR")).to.eq(119);
			expect(calculateSeatId("BBFFBBFRLL")).to.eq(820);
		});
	});
})();
