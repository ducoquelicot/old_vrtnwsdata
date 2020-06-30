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
            left: null,
        }
    }

componentDidMount() {
    this.setSize();
}

setSize = () => {
    if (window.innerWidth > 768) {
        this.setState({top: '480px', left: '47%'})
    }
    else if (window.innerWidth < 768) {
        this.setState({top: '250px', left: '42%'})
    }
}


startSimulation = () => {
    this.setState({ startSim : true});
};

refresh = () => {
    this.setState({ key : Math.random()});
};

render() {

    const { startSim, key, top, left } = this.state;
    const styles = {
        button : {
            display: 'inline-block',
            border: 'none',
            margin: '0',
            textDecoration: 'none',
            background: '#145594',
            color: '#ffffff',
            fontFamily: 'Poppins',
            fontSize: '1rem',
            textAlign: 'center',
            position: 'absolute',
            left: left,
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