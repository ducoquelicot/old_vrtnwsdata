import React from 'react';
import * as d3 from 'd3';
import styles from './style';

export default class Citizen extends React.PureComponent {
  constructor(props) {
    super(props);
    this.references = { citizen: React.createRef() };

    this.state = {
      xCoord : `${Math.round(Math.random() * 90) + 5}%`,
      yCoord : `${Math.round(Math.random() * 90) + 5}%`
    }
  }

  componentDidMount() {
    this.animate();
  }

  componentDidUpdate() {
    this.animate();
  }

  animate() {
    switch (this.props.phase) {
      case 1:
        this.animatePhase1();
        break;
      case 2:
        this.animatePhase2();
        break;
      default:
        this.animatePhase1();
    }
  }

  animatePhase1() {
    const { duration, index, skinTone, guilty } = this.props;
    const steps = 4;
    const timePerStep = duration / steps;
    const delay = (timePerStep * 0.75) * (index / 100);
    const animationTime = timePerStep * 0.25;

    if (skinTone === 'white') {
      d3.select(this.references.citizen.current)
        .style('opacity', 0)
        .transition()
        .delay(timePerStep)
        .transition()
        .delay(delay)
        .duration(animationTime)
        .style('opacity', 0.5);
    }

    if (skinTone === 'black') {
      d3.select(this.references.citizen.current)
        .style('opacity', 0)

        .transition()
        .delay(timePerStep * 2)
        .transition()
        .delay(delay)
        .duration(animationTime)
        .style('opacity', 0.5);
    }

    if (guilty) {
      d3.select(this.references.citizen.current)
        .transition()
        .delay(timePerStep * 3)
        .transition()
        .delay(delay)
        .duration(animationTime * 2)
        .style('stroke', 'red')
        .attr('stroke-width', 3)
        .style('opacity', 0.5);
    }

    d3.select(this.references.citizen.current)
      .transition()
      .delay(duration)
      .duration(animationTime)
      .style('opacity', 0)
  }


  animatePhase2() {
      const { skinTone, count, control } = this.props;
      const rest = count%5;
      const xCoord = skinTone === 'white' ? `${21 + rest * 2}%` : `${71 + rest * 2}%`;
      const yCoord = `${Math.ceil(count/5) * 5 + 15}%`;

      d3.select(this.references.citizen.current)
      .style('opacity', 0)
      
      if (control) {
        d3.select(this.references.citizen.current)
        .transition()
        .delay(700 * count)
        .duration(1000)
        .style('opacity', 1)
        .attr('cx', xCoord)
        .attr('cy', yCoord)
      }
  }

  render() {
    const { skinTone } = this.props;
    const { xCoord, yCoord } = this.state;
    return (
      <circle ref={this.references.citizen} style={styles.circle}
        cx={xCoord}
        cy={yCoord}
        r="10"
        stroke="black"
        fill={skinTone}
        strokeWidth="1"
      />
    );
  }
}
