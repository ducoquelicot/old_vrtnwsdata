import React from 'react';
import Simulation from '../Simulation'
// import styles from './style';

export default class App extends React.PureComponent {
    constructor(props) {
        super(props)

        this.state = {
            startSim : false,
            key: Math.random(),
            top: null,
        }
    }

componentDidMount() {
    this.setSize();
}

setSize = () => {
    if (window.innerWidth < 1300) {
        this.setState({top: '20%'})
    }
    else {
        this.setState({top: '16%'})
    }
}


startSimulation = () => {
    this.setState({ startSim : true});
};

refresh = () => {
    this.setState({ key : Math.random()});
};

render() {

    const { startSim, key, top } = this.state;
    const styles = {
        button : {
            position: 'absolute',
            left: '70%',
            top: top,
        }
    }

    return(
        <div>
            {!startSim && <button onClick={() => this.startSimulation()}>Start</button>}
            {startSim && <button className ="refresh" style={styles.button} onClick={() => this.refresh()}>Refresh</button>}
            {startSim && <Simulation key={key} />}
        </div>
    )
}
}