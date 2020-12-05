import { AdventDay, getInputLines } from "./common";

export default {
	part1(entries: number[]): number {
		entries.sort((a, b) => a - b);
		for (let i = 0; i < entries.length; i++) {
			for (let j = entries.length - 1; j > i; j--) {
				const a = entries[i];
				const b = entries[j];
				const v = a + b;
				if (v === 2020) {
					return a * b;
				}

				if (v < 2020) break;
			}
		}
		throw new Error("Match not found.");
	},
	part2(entries: number[]): number {
		entries.sort((a, b) => a - b);
		for (let i = 0; i < entries.length && entries[i] < 2020 / 3; i++) {
			for (let j = i + 1; j < entries.length && entries[j] < 2020 / 2; j++) {
				for (let k = j + 1; k < entries.length; k++) {
					let r = entries[i] + entries[j] + entries[k];
					if (r === 2020) return entries[i] * entries[j] * entries[k];
				}
			}
		}
		throw new Error("Match not found.");
	},
	async getInput(file: string) {
		return (await getInputLines(file)).map(Number);
	},
} as AdventDay<number[]>;
