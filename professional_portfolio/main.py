import flet as ft

async def main(page: ft.Page):
    # =========================
    # PAGE CONFIGURATION
    # =========================
    page.title = "Academic Web Portfolio - Tulinanye NK Fillipus"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.window_width = 1100
    page.window_height = 850

    # =========================
    # UI COMPONENT HELPERS
    # =========================
    
    def profile_img(path, radius):
        clean_path = path.replace("assets/", "")
        return ft.CircleAvatar(
            foreground_image_src=clean_path,
            radius=radius,
            content=ft.Icon(ft.Icons.PERSON)
        )

    def img(path, w=200):
        clean_path = path.replace("assets/", "")
        return ft.Image(
            src=clean_path,
            width=w,
            fit="contain"  
        )

    def info_card(title, text):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                    ft.Text(text, size=14, color=ft.Colors.BLACK87),
                ],
                spacing=5,
                tight=True
            ),
            padding=20,
            border_radius=12,
            bgcolor="#F5F7FF",
            margin=ft.Margin(left=0, top=0, right=0, bottom=10)
        )

    def contacts_block():
        return ft.Container(
            content=ft.Column(
                [
                    ft.Divider(height=20, thickness=1, color=ft.Colors.BLUE_100),
                    ft.Text("Contact Information", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.EMAIL_OUTLINED, size=20, color=ft.Colors.BLUE_600), 
                            ft.Text("fillipust1@gmail.com", size=14, selectable=True),
                        ],
                        spacing=10
                    ),
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.PHONE_ANDROID_OUTLINED, size=20, color=ft.Colors.BLUE_600), 
                            ft.Text("0813204542", size=14, selectable=True)
                        ],
                        spacing=10
                    ),
                ],
                spacing=10
            ),
            padding=20
        )

    # =========================
    # VIEW DEFINITIONS
    # =========================
    
    def home_view():
        return ft.Column(
            scroll=ft.ScrollMode.ADAPTIVE,
            expand=True,
            controls=[
                ft.Container(
                    content=ft.Row(
                        [
                            profile_img("profile.jpg", 75),
                            ft.Column(
                                [
                                    ft.Text("Tulinanye NK Fillipus", size=26, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                                    ft.Text("Student Number: 225073013", size=15, color=ft.Colors.BLUE_700, weight=ft.FontWeight.W_600),
                                    ft.Text("Degree: B.Eng Mechanical Engineering (Second Year)", size=16, weight=ft.FontWeight.W_500),
                                    ft.Text("University: University of Namibia (UNAM)", size=15),
                                    ft.Text("Group Name: ENGITRIAD", size=15, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_700),
                                ]
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=30
                    ),
                    padding=30,
                ),
                info_card(
                    "Individual Responsibility (Computer Programming I)",
                    "My core contribution to the ENGITRIAD team involved designing backend logical architectures. While our final application is a large group effort (15 members), this individual Web Portfolio assesses my unique personal inputs to our collaborative success."
                ),
                info_card(
                    "Verified Technical Proficiencies",
                    "Python (Flet App Architecture) • Firebase Implementation • MATLAB Numerical Modeling & Data Visualization • GitHub Branch Management & Workflow Documentation"
                ),
                contacts_block(),
            ]
        )

    def timeline_view():
        return ft.Column(
            scroll=ft.ScrollMode.ADAPTIVE,
            expand=True,
            controls=[
                info_card(
                    "Project Timeline (Weekly Log)",
                    "Week 1: Requirement analysis and baseline Flet UI navigation layout protocols.\n"
                    "Week 2: Initializing project sandbox via Git. Designing multi-page view structures.\n"
                    "Week 3: Designing user authentication workflows and secure connection handling.\n"
                    "Week 4: Implementing main data logic operations and state management loops.\n"
                    "Week 5: Configuring internal error handling and validating real-time data sync.\n"
                    "Week 6: Full UI debugging, optimization, and validation against user feedback.\n"
                    "Week 7: Git branch merging and final performance testing reviews.\n"
                    "Week 8: Documentation assembly, asset gathering, and final web configuration."
                ),
                contacts_block(),
            ]
        )

    def github_view():
        return ft.Column(
            scroll=ft.ScrollMode.ADAPTIVE,
            expand=True,
            controls=[
                info_card(
                    "GitHub Evidence & Group Work Verification",
                    "To ensure transparency in our 15-member team, my precise contributions are logged verifiable to my GitHub account ID. I managed clean branch merges and addressed merge conflicts during code integration phases."
                ),
                ft.Text("Verification Snapshot:", weight=ft.FontWeight.W_600),
                img("github.png", 500),
                info_card(
                    "Individual Impact Summary",
                    "My specialized Python and algorithmic work directly resolved data latency errors within our application's Civil Engineering module. This optimized our structural calculation pipelines."
                ),
                contacts_block(),
            ]
        )

    def matlab_view():
        return ft.Column(
            scroll=ft.ScrollMode.ADAPTIVE,
            expand=True,
            controls=[
                info_card(
                    "MATLAB Engineering Mastery",
                    "Proof of completion for 8 separate short self-paced MATLAB courses from the MathWorks Learning Center, focusing on data analysis, numeric computation, and simulation."
                ),
                ft.Text("Verified MathWorks Certificates:", weight=ft.FontWeight.W_600),
                ft.Container(
                    height=280,
                    content=ft.GridView(
                        expand=True,
                        max_extent=180,
                        spacing=10,
                        run_spacing=10,
                        controls=[
                            img("matlab1.png"), img("matlab2.png"),
                            img("matlab3.png"), img("matlab4.png"),
                            img("matlab5.png"), img("matlab6.png"),
                            img("matlab7.png"), img("matlab8.png"),
                        ],
                    )
                ),
                contacts_block(),
            ]
        )

    def blog_view():
        # FIXED: Directly uses the system launcher with a clean web address route
        async def trigger_video_stream(e):
            try:
                # This uses the specific modern service launcher class your error stack traces confirmed
                from flet.controls.services.url_launcher import UrlLauncher
                await UrlLauncher().launch_url("presentation.mp4")
            except Exception:
                # Secondary backup standard method
                await page.launch_url("presentation.mp4")

        return ft.Column(
            scroll=ft.ScrollMode.ADAPTIVE,
            expand=True,
            controls=[
                info_card(
                    "Technical Blog: Confidence in Concepts",
                    "A critical concept in our ENGITRIAD 'OreGuide' module involved automating the corrosion rate calculation for metallurgical analysis."
                ),
                
                ft.Container(
                    content=ft.Column([
                        ft.Text("Core Engineering Formula (Corrosion Rate):", weight=ft.FontWeight.BOLD),
                        ft.Text(
                            "CR = (K × W) / (A × T × D)", 
                            size=20, 
                            weight=ft.FontWeight.BOLD, 
                            color=ft.Colors.BLUE_900
                        ),
                        ft.Text("Where: K=Constant, W=Weight loss, A=Area, T=Time, D=Density", size=12, italic=True)
                    ]),
                    padding=15,
                    bgcolor="#F8F9FA",
                    border_radius=8,
                ),

                info_card(
                    "Project Reflection Video Walkthrough", 
                    "Click the video frame layout window below to initialize the high-definition media rendering stream for my 1:30 presentation."
                ),
                
                ft.Container(
                    width=650,
                    height=360,
                    bgcolor=ft.Colors.BLACK,
                    border_radius=12,
                    padding=20,
                    alignment=ft.Alignment(0, 0),
                    on_click=trigger_video_stream,
                    content=ft.Stack(
                        [
                            ft.Container(
                                alignment=ft.Alignment(0, 0),
                                content=ft.Column(
                                    [
                                        ft.Icon(ft.Icons.VIDEO_CAMERA_FRONT_ROUNDED, size=50, color=ft.Colors.GREY_700),
                                        ft.Text(
                                            "ENGITRIAD Individual Reflection\nClick to Play Video Walkthrough", 
                                            color=ft.Colors.GREY_400, 
                                            size=14, 
                                            text_align=ft.TextAlign.CENTER
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    spacing=12,
                                    tight=True
                                )
                            ),
                            ft.Container(
                                alignment=ft.Alignment(0, 0),
                                content=ft.Container(
                                    content=ft.Icon(ft.Icons.PLAY_ARROW_ROUNDED, size=60, color=ft.Colors.WHITE),
                                    bgcolor="#40000000",
                                    border_radius=40,
                                    padding=10
                                )
                            ),
                            ft.Container(
                                alignment=ft.Alignment(0, 1), 
                                content=ft.Container(
                                    bgcolor="#CC111111",
                                    border_radius=8,
                                    padding=15,
                                    content=ft.Row(
                                        [
                                            ft.Icon(ft.Icons.PLAY_ARROW_ROUNDED, color=ft.Colors.WHITE, size=24),
                                            ft.Text("0:00 / 1:30", color=ft.Colors.WHITE, size=12),
                                            ft.Icon(ft.Icons.FULLSCREEN_ROUNDED, color=ft.Colors.WHITE, size=24),
                                        ],
                                        alignment="spaceBetween",
                                    )
                                )
                            )
                        ]
                    )
                ),
                
                ft.Container(height=15),
                info_card(
                    "Addressing Engineering Obstacles",
                    "Resolution: We addressed network latency issues by deploying local cache rules and unit testing in isolation to ensure systemic data integrity."
                ),
                contacts_block(),
            ]
        )

    # =========================
    # NAVIGATION RAIL MECHANICS
    # =========================
    pages = [
        home_view(),
        timeline_view(),
        github_view(),
        matlab_view(),
        blog_view(),
    ]

    content_area = ft.Container(content=pages[0], expand=True, padding=20)

    def navigation_rail_change(e):
        content_area.content = pages[e.control.selected_index]
        page.update()

    nav_rail = ft.NavigationRail(
        selected_index=0,
        extended=True,
        min_width=100,
        min_extended_width=180,
        label_type=ft.NavigationRailLabelType.ALL,
        on_change=navigation_rail_change,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationRailDestination(icon=ft.Icons.TIMELINE, label="Timeline"),
            ft.NavigationRailDestination(icon=ft.Icons.CODE, label="GitHub Logs"),
            ft.NavigationRailDestination(icon=ft.Icons.SCHOOL, label="MATLAB Hub"),
            ft.NavigationRailDestination(icon=ft.Icons.BOOKMARK_BORDER, label="Tech Blog"),
        ],
    )

    page.add(
        ft.Row(
            [
                ft.Container(content=nav_rail, expand=False, height=800),
                ft.VerticalDivider(width=1),
                content_area,
            ],
            expand=True,
        )
    )

if __name__ == "__main__":
    ft.run(main, assets_dir="assets", view=ft.AppView.WEB_BROWSER)