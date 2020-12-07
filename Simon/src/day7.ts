import { AdventDay, getInputLines } from "./common";

export default {
	part1(input: string[]): number {
		const lookup = input.reduce((p, n) => {
			const split = n.split(" contain ");
			const id = split[0].substr(0, split[0].length - 5);
			const r = /(\d+) ([^.,]+) bags?(?:,|\.)/g;
			let match: RegExpExecArray | null;

			while ((match = r.exec(split[1]))) {
				p[match[2]] = [...(p[match[2]] || []), id];
			}

			return p;
		}, {} as Record<string, string[]>);

		const check = [...lookup["shiny gold"]];
		const uniq = new Set<string>();
		while (check.length) {
			const v = check.pop()!;
			uniq.add(v);
			check.push(...(lookup[v] || []));
		}

		return uniq.size;
	},
	part2(input: string[]): number {
		const rules = input.reduce((p, n) => {
			const split = n.split(" contain ");
			const id = split[0].substr(0, split[0].length - 5);
			const r = /(\d+) ([^.,]+) bags?(?:,|\.)/g;
			let match: RegExpExecArray | null;
			p[id] = {};
			while ((match = r.exec(split[1]))) {
				p[id][match[2]] = +match[1];
			}

			return p;
		}, {} as Record<string, Record<string, number>>);

		const calculate = (bag: string): number => {
			const bags = rules[bag];
			return Object.keys(bags).reduce((p, b) => {
				return p + calculate(b) * bags[b];
			}, 1);
		};

		return calculate("shiny gold") - 1;
	},
	async getInput(file: string) {
		return await getInputLines(file, "\r\n");
	},
} as AdventDay<string[]>;
