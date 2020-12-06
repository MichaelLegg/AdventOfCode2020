import { AdventDay, getInputLines } from "./common";

export default {
	part1(input: string[]): number {
		return input.reduce(
			(p, n) => p + new Set([...n.replace(/\s/g, "")]).size,
			0
		);
	},
	part2(input: string[]): number {
		return input.reduce((p, n) => {
			const grouped = n
				.split(/\n|/g)
				.reduce(
					(a, b) => ((a[b] = b in a ? a[b] + 1 : 1), a),
					{} as Record<string, number>
				);

			const people = n.split(/\r\n/g);
			return (
				p +
				Object.keys(grouped).filter((g) => grouped[g] === people.length).length
			);
		}, 0);
	},
	async getInput(file: string) {
		return await getInputLines(file, "\r\n\r\n");
	},
} as AdventDay<string[]>;
