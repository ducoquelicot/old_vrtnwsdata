import React from 'react';
import Human from '../../generators/Human';
import Citizen from '../Citizen';
import Narrator from '../Narrator';
import styles from './style';
import Titles from '../Titles';
import Bars from '../Bars';
import { rng } from '../../generators/Human/numgen';

export default class Simulation extends React.PureComponent {

  constructor(props) {
    super(props);
    this.citizenAmount = 1000;
    this.durationPhase1 = 10000; // ms
    this.durationPhase2 = 10000; // ms
    this.durationPhase3 = 10000; // ms
    this.delayBetweenPhases = 1000; //ms

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
  }

  startPhaseCountdown() {
    const delayPhase2 = this.durationPhase1 + this.delayBetweenPhases;
    const delayPhase3 = this.durationPhase1 + this.durationPhase2 + (this.delayBetweenPhases * 2);

    setTimeout(() => {
      console.log(this.state.citizens)
      const countWhite = this.state.citizens.filter(citizen => citizen.control && citizen.guilty && citizen.skinTone === 'white').length 
      const countBlack = this.state.citizens.filter(citizen => citizen.control && citizen.guilty && citizen.skinTone === 'black').length  

      const totalWhite = this.state.citizens.filter(citizen => citizen.control && citizen.skinTone === 'white').length
      const totalBlack = this.state.citizens.filter(citizen => citizen.control && citizen.skinTone === 'black').length

      const percentageWhite = countWhite / totalWhite * 100
      const percentageBlack = countBlack / totalBlack * 100

      this.setState({ 
        duration: this.durationPhase2, 
        phase: 2,
        percentageWhite,
        percentageBlack,
      });
    }, delayPhase2);

    setTimeout(() => {
      this.setState({ duration: this.durationPhase3, phase: 3 });
    }, delayPhase3);
  }

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
        const previous = arr[i-1]

        if (citizen.skinTone === 'white') {
          controlChance = () => Math.random() >= 0.9;
          citizen.control = controlChance();
        }
        else if (previous === undefined && citizen.skinTone === 'black') {
          var controlChance = () => Math.random() >= 0.2;
          citizen.control = controlChance();
        }
        else if (previous.skinTone === 'black' && citizen.skinTone === 'black') {
          citizen.control = 0.1;
        }
        else if (previous.guilty === true && previous.skinTone === 'black' && citizen.skinTone === 'black') {
          citizen.control = true;
        }

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
