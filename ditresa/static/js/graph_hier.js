/**
 * graph_hier.js
 *** Util forms user-defined hierarchical graph layout.***
 * All initial data are transfered by JSON from server through html. 
 */
    var nodes = null;
    var edges = null;
    var network = null;
    var directionInput = document.getElementById("direction");


    function destroy() {
      if (network !== null) {
          network.destroy();
          network = null;
      }
    }

    function draw() {
      destroy();
      nodes = [];
      edges = [];
      var connectionCount = [];

      // Variables from server
      var planets = js_planets;
      var planet_simbol = js_planet_simbol;
      var planet_control0 = js_planet_control;
      var planet_level0 = js_planet_level;
      var len_planets = planets.length

      for (var i = 0; i < len_planets; i++) {
        // Nodes construction
        nodes.push({
          id: planets[i], 
          label: planet_simbol[planets[i]],
          level: planet_level0[planets[i]],
          font: {size:50},
          shape: 'circle'
        });
        // Edges construction
        edges.push({
          from: planets[i], 
          to: planet_control0[planets[i]], 
          arrows:'to' 
        });
      }

      // create a network
      var container = document.getElementById('graph_container');

      // provide data in the vis format
      var data = {
        nodes: nodes,
        edges: edges
      };

      var options = {
        // height: '50%',
        // width: '50%',
        // align: 'left',
        edges: {
            smooth: true
        },
        layout: {
          hierarchical:{
              direction: directionInput.value
          }
        }
      };
      network = new vis.Network(container, data, options);

      // add event listeners
      network.on('select', function(params) {
        document.getElementById('selection').innerHTML = 'Selection: ' + params.nodes;
      });
    }
