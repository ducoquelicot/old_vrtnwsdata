import React from 'react';
import * as d3 from 'd3';
import styles from './style';

export default class Citizen extends React.PureComponent {
  constructor(props) {
    super(props);
    this.xCoord = `${Math.round(Math.random() * 90) + 5}%`;
    this.yCoord = `${Math.round(Math.random() * 90) + 5}%`;
    this.references = { citizen: React.createRef() };
  }

  componentDidMount() {
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
        .style('opacity', 1.0);
    }

    if (skinTone === 'black') {
      d3.select(this.references.citizen.current)
        .style('opacity', 0)

        .transition()
        .delay(timePerStep * 2)
        .transition()
        .delay(delay)
        .duration(animationTime)
        .style('opacity', 1.0);
    }

    if (guilty) {
      d3.select(this.references.citizen.current)
        .transition()
        .delay(timePerStep * 3)
        .transition()
        .delay(delay)
        .duration(animationTime * 2)
        .style('stroke', 'red')
        .attr('stroke-width', 5);
    }
  }

  animatePhase2() {

  }

  render() {
    const { skinTone } = this.props;
    return (
      <circle ref={this.references.citizen} style={styles.circle}
        cx={this.xCoord}
        cy={this.yCoord}
        r="0.75%"
        stroke="black"
        fill={skinTone}
        strokeWidth="1"
      />
    );
  }
}
