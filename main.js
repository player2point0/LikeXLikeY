const EDGE_SIZE = 1;
const NODE_SIZE_MULTI = 1;

let g = {
	nodes: [],
	edges: [],
};

//todo group related points
const JSON_BIN_VERSION = 5;

//edit json : https://jsonbin.io/5f0f4f76918061662842419c/1
fetch("https://api.jsonbin.io/b/5f0f4f76918061662842419c/" + JSON_BIN_VERSION)
	.then((response) => response.json())
	.then((data) => renderGraph(data.data))
	.catch((error) => console.error(error));

function renderGraph(DATA) {
	console.log(DATA);

	for (let i = 0; i < DATA.length; i++) {
		const name = DATA[i].name;
		const x = DATA[i].x ? DATA[i].x : Math.random();
		const y = DATA[i].y ? DATA[i].y : Math.random();

		if (!name) continue;

		const numConnections = DATA[i].like.length;
		const size =
			numConnections > 0 ? numConnections * NODE_SIZE_MULTI : NODE_SIZE_MULTI;

		g.nodes.push({
			id: "n:" + name,
			label: name,
			x: x,
			y: y,
			size: size,
			color: "#666",
		});

		for (let j = 0; j < DATA[i].like.length; j++) {
			const likeName = DATA[i].like[j];

			g.edges.push({
				id: "e:" + name + ":" + likeName,
				source: "n:" + name,
				target: "n:" + likeName,
				size: EDGE_SIZE,
				color: "#ccc",
			});
		}
	}

	// Instantiate sigma:
	const s = new sigma({
		graph: g,
		container: "graph-container",
	});
}
