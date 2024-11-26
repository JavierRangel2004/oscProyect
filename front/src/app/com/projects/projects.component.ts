// src/app/com/projects/projects.component.ts
import { Component, OnInit } from '@angular/core';
import { ProjectService } from '../../services/project.service';
import { Project } from '../../models/project';

@Component({
  selector: 'app-projects',
  templateUrl: './projects.component.html',
  styleUrls: ['./projects.component.css'],
})
export class ProjectsComponent implements OnInit {
  projects: Project[] = [];

  constructor(private projectService: ProjectService) {}

  // src/app/com/projects/projects.component.ts
  ngOnInit(): void {
    this.projectService.getProjects().subscribe(
      (data) => {
        this.projects = data.sort((a, b) => a.name.localeCompare(b.name));
      },
      (error) => console.error('Error fetching projects', error)
    );
  }
}
