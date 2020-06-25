import React from 'react';
import * as d3 from 'd3';
import styles from "./style.js";

export default class Titles extends React.PureComponent {
  constructor(props) {
    super(props);
    this.references = { 
      title1: React.createRef(),
      title2: React.createRef()
    };
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
    d3.select(this.references.title1.current)
      .style('opacity', 0)

    d3.select(this.references.title2.current)
    .style('opacity', 0)
  }

  animatePhase2() {
    const { duration} = this.props;
    const steps = 4;
    const timePerStep = duration / steps;
    const delay = timePerStep * 0.5;
    const animationTime = timePerStep * 0.25;

    d3.select(this.references.title1.current)
    .transition()
    .delay(delay)
    .duration(animationTime)
    .style('opacity', 1.0)

    d3.select(this.references.title2.current)
    .transition()
    .delay(delay)
    .duration(animationTime)
    .style('opacity', 1.0)
  }

  render() {
    return (
      <g>
      <text ref={this.references.title1}
        x= "25%"
        y= "10%"
        width="50%"
        height="10%"
        style={styles.text}
        >
          Witte mensen
        </text>

      <text ref={this.references.title2}
        x= "75%"
        y= "10%"
        width="50%"
        height="10%"
        style={styles.text}
        >
          Zwarte mensen
        </text>
      </g>
    );
  }
}
