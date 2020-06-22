import React from 'react';
import Human from '../../generators/Human';
import Citizen from '../Citizen';
import Narrator from '../Narrator';

export default class Simulation extends React.PureComponent {

  constructor(props) {
    super(props);
    this.citizenAmount = 100;
    this.durationPhase1 = 25000; // ms
    this.durationPhase2 = 10000; // ms
    this.durationPhase3 = 10000; // ms
    this.delayBetweenPhases = 5000; //ms

    this.state = {
      citizens: [],
      phase: 1,
      duration: this.durationPhase1
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
      this.setState({ duration: this.durationPhase2, phase: 2 });
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

    return (
      citizens.map(citizen => {
        return <Citizen
          key={citizen.index}
          index={citizen.index}
          duration={duration}
          phase={phase}
          skinTone={citizen.skinTone}
          guilty={citizen.guilty}
          name={citizen.name}
        />;
      })
    );
  }

  render() {
    const { duration } = this.state;
    const citizens = this.renderCitizens();

    console.log(this.state);
    return (
      <svg>
        {citizens}
        <Narrator phase={this.phase} duration={duration} />
      </svg>
    );
  }
}
