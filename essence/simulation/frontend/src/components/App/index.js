import React from 'react';
import Simulation from '../Simulation'

export default class App extends React.PureComponent {
    constructor(props) {
        super(props)

        this.state = {
            startSim : false,
            key: Math.random(),
        }
    }


startSimulation = () => {
    this.setState({ startSim : true});
};

refresh = () => {
    this.setState({ key : Math.random()});
};

render() {

    const { startSim, key } = this.state;

    return(
        <div>
            {!startSim && <button onClick={() => this.startSimulation()}>Start</button>}
            {startSim && <Simulation key={key} />}
            {startSim && <button onClick={() => this.refresh()}>Refresh</button>}
        </div>
    )
}
}