// src/app/com/organizations/organizations.component.ts
import { Component, OnInit } from '@angular/core';
import { OrganizationService } from '../../services/organization.service';
import { Organization } from '../../models/organization';

@Component({
  selector: 'app-organizations',
  templateUrl: './organizations.component.html',
  styleUrl: './organizations.component.css'
})
export class OrganizationsComponent implements OnInit {
  organizations: Organization[] = [];

  constructor(private organizationService: OrganizationService) {}

  ngOnInit(): void {
    this.organizationService.getOrganizations().subscribe(
      (data) => {
        this.organizations = data.sort((a, b) =>
          a.name.localeCompare(b.name)
        );
      },
      (error) => console.error('Error fetching organizations', error)
    );
  }
}
