import { AdventDay } from "./common";

(async () => {
	const day = +process.argv[process.argv.length - 1];
	if (isNaN(day)) {
		console.error(
			"usage: npm start -- {day}\nwhere{day} is a completed challenge, e.g. npm start -- 1"
		);
	} else {
		const mod = (await import("./day" + day)).default as AdventDay<unknown>;
		console.log(
			"Part 1:",
			mod.part1(await mod.getInput(`../data/day${day}.txt`))
		);
		console.log(
			"Part 2:",
			mod.part2(await mod.getInput(`../data/day${day}.txt`))
		);
	}
})();
