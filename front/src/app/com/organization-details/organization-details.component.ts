// src/app/com/organization-details/organization-details.component.ts
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { OrganizationService } from '../../services/organization.service';
import { ProjectService } from '../../services/project.service';
import { Organization } from '../../models/organization';
import { Project } from '../../models/project';

@Component({
  selector: 'app-organization-details',
  templateUrl: './organization-details.component.html',
  styleUrls: ['./organization-details.component.css'],
})
export class OrganizationDetailsComponent implements OnInit {
  organization: Organization | null = null;
  projects: Project[] = [];

  constructor(
    private route: ActivatedRoute,
    private organizationService: OrganizationService,
    private projectService: ProjectService
  ) {}

  // src/app/com/organization-details/organization-details.component.ts
  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.organizationService.getOrganization(id).subscribe(
      (data) => {
        this.organization = data;
        // Fetch projects for this organization
        this.projectService.getProjectsByOrganization(id).subscribe(
          (projects) => (this.projects = projects),
          (error) => console.error('Error fetching projects for organization', error)
        );
      },
      (error) => console.error('Error fetching organization', error)
    );
  }

}
