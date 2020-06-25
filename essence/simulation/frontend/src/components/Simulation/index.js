import React from 'react';
import Human from '../../generators/Human';
import Citizen from '../Citizen';
import Narrator from '../Narrator';
import styles from './style';
import Titles from '../Titles';
import Bars from '../Bars';

export default class Simulation extends React.PureComponent {

  constructor(props) {
    super(props);
    this.citizenAmount = 100;
    this.durationPhase1 = 15000; // ms
    this.durationPhase2 = 10000; // ms
    // this.durationPhase3 = 10000; // ms
    this.delayBetweenPhases = 5000; //ms

    this.state = {
      citizens: [],
      phase: 1,
      duration: this.durationPhase1,
      percentageWhite: 0,
      percentageBlack: 0,
    };
  }

  componentDidMount() {
    this.generatePopulation();
    this.startPhaseCountdown();
    // this.restartViz();
  }

  startPhaseCountdown() {
    const delayPhase2 = this.durationPhase1 + this.delayBetweenPhases;

    setTimeout(() => {
      console.log(this.state.citizens)
      const countWhite = this.state.citizens.filter(citizen => citizen.control && citizen.guilty && citizen.skinTone === 'white').length;
      const countBlack = this.state.citizens.filter(citizen => citizen.control && citizen.guilty && citizen.skinTone === 'black').length;  

      const totalGuilty = this.state.citizens.filter(citizen => citizen.control && citizen.guilty).length;

      const percentageWhite = countWhite / totalGuilty * 100;
      const percentageBlack = countBlack / totalGuilty * 100;

      this.setState({ 
        duration: this.durationPhase2, 
        phase: 2,
        percentageWhite,
        percentageBlack,
      });

    }, delayPhase2);
  }

  // restartViz() {
  //   const totalDuration = this.durationPhase1 + this.delayBetweenPhases + this.durationPhase2 + 1000;

  //   setInterval(() => {
  //     this.setState = ({
  //       citizens: [],
  //       phase: 1,
  //       duration: this.durationPhase1,
  //       percentageWhite: 0,
  //       percentageBlack: 0,
  //     });
  //   }, totalDuration);

  //   this.generatePopulation();
  //   this.startPhaseCountdown();
  // }

  generatePopulation() {
    const population = [];
    for (let index = 0; index < this.citizenAmount; index++) {
      population.push(new Human({ index }));
    }
    this.setState({ citizens: population });
  }

  renderCitizens() {
    const { citizens, duration, phase } = this.state;

    let whiteCount = 0
    let blackCount = 0

    return (
      citizens.map((citizen, i, arr) => {
        // scenario 3
        // const previous = arr[i-1]

        // if (citizen.skinTone === 'white') {
        //   var controlChance = () => Math.random() >= 0.8;
        //   citizen.control = controlChance();
        // }
        // else if (previous === undefined && citizen.skinTone === 'black') {
        //   controlChance = () => Math.random() >= 0.2;
        //   citizen.control = controlChance();
        // }
        // else if (previous.skinTone === 'black' && citizen.skinTone === 'black') {
        //   controlChance = () => Math.random() >= 0.1;
        //   citizen.control = controlChance();
        // }
        // else if (previous.skinTone === 'white' && citizen.skinTone === 'black') {
        //   controlChance = () => Math.random() >= 0.2;
        //   citizen.control = controlChance();
        // }

        whiteCount = citizen.skinTone === 'white' && citizen.control ? whiteCount + 1 : whiteCount
        blackCount = citizen.skinTone === 'black' && citizen.control ? blackCount + 1 : blackCount
        
        return <Citizen
          key={citizen.index}
          index={citizen.index}
          duration={duration}
          phase={phase}
          skinTone={citizen.skinTone}
          guilty={citizen.guilty}
          name={citizen.name}
          count={citizen.skinTone === 'white' ? whiteCount : blackCount}
          control={citizen.control}
        />;
      })
    );
  }

  render() {
    const { duration, phase, percentageBlack, percentageWhite } = this.state;
    const citizens = this.renderCitizens();

    console.log(this.state);
    return (
      <svg style={styles.svg}>
        {citizens}
        <Narrator phase={phase} duration={duration} />
        <Titles phase={phase} duration={duration} />
        <Bars phase={phase} duration={duration} percentageWhite={percentageWhite} percentageBlack={percentageBlack} />
      </svg>
    );
  }
}
