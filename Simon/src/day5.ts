import { AdventDay, getInputLines } from "./common";

export function calculateSeatId(pass: string): number {
	return parseInt(pass.replace(/B|R/g, "1").replace(/F|L/g, "0"), 2);
}

export default {
	part1(input: string[]): number {
		return input.map(calculateSeatId).sort((a, b) => b - a)[0];
	},
	part2(input: string[]): number {
		const seats = input.map(calculateSeatId).sort((a, b) => a - b);
		for (let i = seats[0]; i < seats[seats.length - 1]; i++) {
			if (!seats.includes(i)) {
				return i;
			}
		}
		throw new Error("Unable to find missing seat");
	},
	async getInput(file: string) {
		return await getInputLines(file, "\r\n");
	},
} as AdventDay<string[]>;
