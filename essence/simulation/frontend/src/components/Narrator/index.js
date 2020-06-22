import React from 'react';
import * as d3 from 'd3';

export default class Narrator extends React.PureComponent {
  constructor(props) {
    super(props);
    this.references = { text1: React.createRef() };
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
    const { duration } = this.props;
    const steps = 4;
    const timePerStep = duration / steps;
    const delay = timePerStep * 0.5;
    const animationTime = timePerStep * 0.25;

    d3.select(this.references.text1.current)
      .style('opacity', 0)

      .transition()
      .duration(animationTime)
      .style('opacity', 1)
      .text('Hier zijn 100 mensen')
      .transition()
      .delay(delay)
      .duration(animationTime)
      .style('opacity', 0)

      .transition()
      .duration(animationTime)
      .style('opacity', 1)
      .text('Sommigen zijn blank')
      .transition()
      .delay(delay)
      .duration(animationTime)
      .style('opacity', 0)

      .transition()
      .duration(animationTime)
      .style('opacity', 1)
      .text('Sommigen zijn zwart')
      .transition()
      .delay(delay)
      .duration(animationTime)
      .style('opacity', 0)

      .transition()
      .duration(animationTime)
      .style('opacity', 1)
      .text('Sommigen zijn schuldig')
      .transition()
      .delay(delay)
      .duration(animationTime)
      .style('opacity', 0);
  }

  animatePhase2() {

  }

  render() {
    return (
      <text ref={this.references.text1}
        className='narrator'
        x='50%'
        y='50%'
      />
    );
  }
}
